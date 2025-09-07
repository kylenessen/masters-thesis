## Power Analysis for Wind Effect
A common concern with non-significant results is whether the study had enough statistical power to detect an effect if one truly existed. A low R-squared value (like the 5.6% in our best model) is common in ecological studies with high natural variability and doesn't invalidate the model, but it does make power a relevant question.

To address this, we can perform a simulation-based power analysis. This is a modern approach, especially for complex models like GAMs. The process is as follows:

1.  **Simulate Data from the Null Hypothesis:** We take our best-fitting model (which does *not* include wind) and use it to generate hundreds of new, simulated datasets. These datasets have the same characteristics as our real data, but we know for a fact that there is no wind effect in them.
2.  **Add a Known Wind Effect:** To each simulated dataset, we artificially add a wind effect of a specific size. We'll test several sizes, from small to medium, to see what our model is sensitive to.
3.  **Re-run the Analysis:** We fit a GAM that *does* include a wind term to each of these new datasets.
4.  **Calculate Power:** We calculate the percentage of these simulations in which we correctly detect the artificial wind effect as statistically significant (p < 0.05). This percentage is our statistical power.

If we have high power to detect a small or medium-sized effect, it strengthens our conclusion that the true effect of wind is likely negligible or non-existent. If we only have power to detect a very large effect, our conclusions are weaker.

```{r}
#| label: power-analysis
#| cache: true
#| warning: false
#| message: false

cat("Starting power analysis for wind effect...\n")

# Define effect sizes. These are defined in terms of the standard deviation of the response variable.
# An effect size of 0.1 means we are testing if we can detect a scenario where a 1 standard deviation
# increase in wind speed causes a 0.1 standard deviation change in the response.
sd_response <- sd(model_data$butterfly_difference_cbrt, na.rm = TRUE)
effect_sizes_to_test <- c(0.05, 0.1, 0.15, 0.2)

# Simulation parameters
n_sims <- 200 # For final results.
alpha <- 0.05

# Get predictions and residual SD from the best model (which does not include wind)
# This will serve as the basis for our simulations.
base_predictions <- predict(best_model$gam, newdata = model_data)
residual_sd <- summary(best_model$gam)$scale

# Store results
power_results <- list()

# Main simulation loop
for (effect_size_coef in effect_sizes_to_test) {
    
    # This is the actual effect size we're adding to the model
    current_effect_size <- effect_size_coef * sd_response
    
    cat("Testing effect size:", round(effect_size_coef, 2), " (SD units): ")
    
    p_values <- numeric(n_sims) # initialize vector

    # Replicate the simulation `n_sims` times
    for (i in 1:n_sims) {
        if (i %% 10 == 0) cat(i, "/", n_sims, "... ")

        # Simulate a new response variable based on the best model's predictions and residuals
        simulated_response <- rnorm(nrow(model_data), mean = base_predictions, sd = residual_sd)

        # Add the artificial wind effect. We scale max_gust so the effect size is standardized.
        wind_effect <- current_effect_size * scale(model_data$max_gust)
        response_with_effect <- simulated_response + as.vector(wind_effect)

        # Create a temporary dataset for fitting
        sim_data <- model_data
        sim_data$sim_response <- response_with_effect

        # Fit the GAM model that includes the wind term
        # This is the same structure as your second-best model
        power_model_formula <- as.formula(
            "sim_response ~ s(total_butterflies_t_lag) + s(max_gust) + s(temperature_avg) + s(butterflies_direct_sun_t_lag) + s(time_within_day_t)"
        )
        
        # Use tryCatch to handle potential model fitting errors in simulations
        fit <- tryCatch({
            gamm(
                power_model_formula,
                data = sim_data,
                random = random_structure,
                correlation = correlation_structure,
                method = "REML"
            )
        }, error = function(e) NULL)

        # Extract the p-value for the wind term if the model converged
        if (!is.null(fit)) {
            p_values[i] <- summary(fit$gam)$s.table["s(max_gust)", "p-value"]
        } else {
            p_values[i] <- NA # Return NA if model failed
        }
    }
    cat("Done.\n")

    # Calculate power: the proportion of simulations where the effect was detected (p < alpha)
    # We remove any NA p-values from failed model fits
    power <- mean(p_values < alpha, na.rm = TRUE)
    power_results[[as.character(effect_size_coef)]] <- power
}

cat("Power analysis complete.\n")

# Format and display the results
power_df <- data.frame(
    EffectSize_SD_units = as.numeric(names(power_results)),
    Power = unlist(power_results)
) %>%
    mutate(
        Power_Percent = paste0(round(Power * 100, 1), "%" )
    )

kable(power_df, 
      caption = "Estimated power to detect a given effect size for the `max_gust` term. Effect size is measured in standard deviations of the response variable.",
      col.names = c("Effect Size (in SD units)", "Power (Proportion)", "Power (%)"))

```