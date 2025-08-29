# Temperature Data Extraction and Cleaning Methods - Research Findings

## Overview
Research conducted on two GitHub branches (`extract-temp` and `clean-temperature-extraction-data`) that contain the complete methodology for extracting and cleaning temperature data from trail camera images for a monarch butterfly thesis project.

## Branch 1: extract-temp - OCR-Based Temperature Extraction Enhancement

### Primary Development
**File**: `python-tools/extract-temp/extract_temp.py`
**Commit**: "Enhance temperature extraction with retry logic and improved OCR handling" (b3c6fb9)

### Key Technical Innovations

#### 1. Multi-Strategy Retry System
- Implemented 4-stage retry mechanism with progressively different approaches:
  - **Strategy 1**: Original approach (90% height crop, 40% width, moderate preprocessing)
  - **Strategy 2**: Larger bounding box (88% height, 50% width, aggressive preprocessing)
  - **Strategy 3**: Even larger box (85% height, 60% width, different EasyOCR thresholds)
  - **Strategy 4**: Full bottom strip (92% height, full width, minimal preprocessing)

#### 2. Enhanced OCR Processing
- **EasyOCR parameter tuning**: Implemented variable `width_ths` and `height_ths` parameters for better text detection
- **Image preprocessing pipeline**: Variable contrast enhancement (1.2-2.0x) and brightness adjustment (1.1-1.4x)
- **GPU acceleration**: Utilized EasyOCR with GPU support for faster processing

#### 3. Robust Pattern Matching
Developed comprehensive regex patterns to handle OCR variations:
- Primary pattern: `(\d+)\s*[°\'·]?\s*C` (handles °C, ·C, 'C variations)
- Temperature display pattern: `T\s+(\d+)\s*[°\'·]?\s*C` (for "T 12 °C" format)
- Celsius/Fahrenheit pattern: `(\d+)\s*[°\'·]?\s*C\s*/\s*\d+\s*[°\'·]?\s*F`
- Context-aware pattern: `(\d+)\s*[^\w\s]*\s*C(?:\s|/|\s*\d)` (handles symbol misreads)

#### 4. Improved Data Handling
- **Enhanced deployment ID extraction**: Fixed parsing of underscored deployment names (e.g., "SLC6_1_20240105142001.JPG" → "SLC6_1")
- **Timestamp extraction**: Robust 14-digit timestamp parsing from filenames
- **Validation system**: Temperature range validation (0-100°C) with confidence scoring

#### 5. Performance Metrics
- **Success rate improvement**: From ~80% to 92%+ on test datasets
- **Processing efficiency**: Batch processing with progress tracking via tqdm
- **Output format**: CSV with filename, deployment_id, timestamp, temperature, confidence, extraction_status

## Branch 2: clean-temperature-extraction-data - Systematic Data Cleaning

### Dataset Characteristics
- **Total records**: ~56,000 temperature readings from multiple trail camera deployment sites
- **Primary data quality issues**: Missing values (~170 records), extreme outliers (≥35°C or ≤2°C), temporal discontinuities

### 5-Phase Cleaning Methodology

#### Phase 1: Initial Data Exploration
**Tool**: `data_exploration.py`
- **Threshold-based outlier detection**: Automated identification of extreme values
- **Visualization**: Time series plots for each deployment site
- **Missing value quantification**: Identified ~170 completely failed OCR extractions

#### Phase 2: Manual Entry for Missing Values
**Tool**: `manual_temperature_entry.py` (Custom tkinter GUI)
**Features**:
- Image-by-image display of trail camera photos
- Temperature input field with Celsius validation
- Navigation controls (keyboard shortcuts: Enter, Left/Right arrows)
- Progress tracking and session persistence
- **Output**: Entries marked with confidence=1.0 and extraction_status="manual_entry"

#### Phase 3: Extreme Outlier Correction
**Process**: Used same GUI tool for systematic review of outliers
- **Target values**: Temperatures ≥35°C (suspected Fahrenheit conversion errors) or ≤2°C (OCR misreads)
- **Validation approach**: Manual verification against source images
- **Output**: `manual_extreme_temperature_entries.csv`

#### Phase 4: Temporal Discontinuity Detection
**Tool**: `manual_review.py` (Interactive Dash web application with Plotly)
**Features**:
- **Deployment-specific time series visualization**: Interactive plots for each camera site
- **Point-and-click selection**: Click suspicious temperature spikes/drops for flagging
- **Iterative review process**: Multiple passes to catch remaining discontinuities
- **Export functionality**: Deployment-specific CSV files for follow-up (e.g., `SC2_followup.csv`, `SC4_followup.csv`)

#### Phase 5: Final Data Integration
**Tool**: `clean_temperature_data.py`
**Hierarchical merging approach**:
1. Original OCR data (baseline)
2. Missing value corrections
3. Extreme outlier corrections
4. Temporal discontinuity corrections
**Conflict resolution**: Manual entries (confidence=1.0) always override automated OCR values

### Key Technical Decisions

#### Data Integrity Preservation
- **Non-destructive approach**: Original source data never modified
- **Overlay methodology**: Corrections applied as separate files with hierarchical merging
- **Audit trail**: Full traceability of all modifications

#### Manual Entry Over Re-OCR
- **Rationale**: Given initial OCR failure rates, manual verification provided higher reliability
- **Implementation**: Custom GUI tools optimized for efficient systematic review

#### Confidence-Based Data Management
- **Manual entries**: confidence=1.0 (highest priority)
- **Original OCR**: variable confidence scores
- **Merging logic**: Higher confidence values always override lower ones

### Quality Assurance Process
1. **Visual validation**: Time series plots generated after each cleaning phase
2. **Iterative review**: Multiple passes through interactive review tool
3. **Spot checking**: Manual verification confirmed accuracy of both corrections and originally suspected values determined to be correct
4. **Cross-validation**: Some initially flagged values verified as accurate upon image inspection

### Documentation Created
- **`METHODS.md`**: Comprehensive 127-line methodology document detailing all cleaning phases
- **`Workflow_for_Manual_Temperature_Data_Cleaning.md`**: Step-by-step workflow documentation
- Multiple deployment-specific correction CSV files preserving all manual entries

## Software Tools Developed

### Core Extraction Tool
- **`extract_temp.py`**: 409-line comprehensive OCR pipeline with retry logic and robust pattern matching

### Data Cleaning Tools
- **`manual_temperature_entry.py`**: GUI application for systematic manual data entry
- **`manual_review.py`**: Interactive web-based tool for temporal pattern analysis and discontinuity detection
- **`check_extreme_temps.py`**: Automated extreme value detection and visualization

### Supporting Scripts
- Various data exploration, merging, and validation utilities
- Deployment-specific analysis tools

## Final Dataset Quality Metrics
- **Missing values**: Eliminated through systematic manual entry
- **Extreme outliers**: Corrected through manual verification
- **Temporal discontinuities**: Identified and corrected through iterative interactive review
- **Data completeness**: ~56,000 cleaned temperature readings
- **Methodology**: Fully documented and reproducible cleaning pipeline

## Technical Stack
- **OCR**: EasyOCR with GPU acceleration
- **GUI**: tkinter for manual entry interface
- **Web interface**: Dash + Plotly for interactive data review
- **Data processing**: pandas, PIL, numpy
- **Validation**: Custom temperature range validation (0-100°C)
- **Version control**: Systematic branching with detailed commit messages documenting each phase