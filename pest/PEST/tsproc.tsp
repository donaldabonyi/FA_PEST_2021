#############
# Settings Block
START SETTINGS
   CONTEXT model_post
   DATE_FORMAT dd/mm/yyyy
END SETTINGS

# Read Time Series (model output)
START GET_MUL_SERIES_SSF
   CONTEXT all
   FILE ../PFLOTRAN/pflotran_output.ssf
   SITE obs_1
   NEW_SERIES_NAME temp_model_site1
   SITE obs_2
   NEW_SERIES_NAME temp_model_site2
   SITE obs_3
   NEW_SERIES_NAME temp_model_site3
   SITE obs_4
   NEW_SERIES_NAME temp_model_site4
   SITE obs_5
   NEW_SERIES_NAME temp_model_site5
   SITE obs_6
   NEW_SERIES_NAME temp_model_site6
   SITE obs_7
   NEW_SERIES_NAME temp_model_site7
   SITE obs_8
   NEW_SERIES_NAME temp_model_site8
   SITE obs_9
   NEW_SERIES_NAME temp_model_site9
   SITE obs_10
   NEW_SERIES_NAME temp_model_site10
   SITE obs_11
   NEW_SERIES_NAME temp_model_site11
   SITE obs_12
   NEW_SERIES_NAME temp_model_site12
   SITE obs_13
   NEW_SERIES_NAME temp_model_site13
   SITE obs_14
   NEW_SERIES_NAME temp_model_site14
   SITE obs_15
   NEW_SERIES_NAME temp_model_site15
   SITE obs_16
   NEW_SERIES_NAME temp_model_site16
   SITE obs_17
   NEW_SERIES_NAME temp_model_site17
   SITE obs_18
   NEW_SERIES_NAME temp_model_site18
   SITE obs_19
   NEW_SERIES_NAME temp_model_site19
   SITE obs_20
   NEW_SERIES_NAME temp_model_site20
   SITE obs_21
   NEW_SERIES_NAME temp_model_site21
   SITE obs_22
   NEW_SERIES_NAME temp_model_site22
   SITE obs_23
   NEW_SERIES_NAME temp_model_site23
   SITE obs_24
   NEW_SERIES_NAME temp_model_site24
   SITE obs_25
   NEW_SERIES_NAME temp_model_site25
   SITE obs_26
   NEW_SERIES_NAME temp_model_site26
   SITE obs_27
   NEW_SERIES_NAME temp_model_site27
   SITE obs_28
   NEW_SERIES_NAME temp_model_site28
   SITE obs_29
   NEW_SERIES_NAME temp_model_site29
   SITE obs_30
   NEW_SERIES_NAME temp_model_site30
   SITE obs_31
   NEW_SERIES_NAME temp_model_site31
   SITE obs_32
   NEW_SERIES_NAME temp_model_site32
   SITE obs_33
   NEW_SERIES_NAME temp_model_site33
   SITE obs_34
   NEW_SERIES_NAME temp_model_site34
   SITE obs_35
   NEW_SERIES_NAME temp_model_site35
   SITE obs_36
   NEW_SERIES_NAME temp_model_site36
   SITE obs_37
   NEW_SERIES_NAME temp_model_site37
   SITE obs_38
   NEW_SERIES_NAME temp_model_site38
   SITE obs_39
   NEW_SERIES_NAME temp_model_site39
   SITE obs_40
   NEW_SERIES_NAME temp_model_site40
   SITE obs_41
   NEW_SERIES_NAME temp_model_site41
   SITE obs_42
   NEW_SERIES_NAME temp_model_site42
   SITE obs_43
   NEW_SERIES_NAME temp_model_site43
   SITE obs_44
   NEW_SERIES_NAME temp_model_site44
   SITE obs_45
   NEW_SERIES_NAME temp_model_site45
   SITE obs_46
   NEW_SERIES_NAME temp_model_site46
   SITE obs_47
   NEW_SERIES_NAME temp_model_site47
   SITE obs_48
   NEW_SERIES_NAME temp_model_site48
   SITE obs_49
   NEW_SERIES_NAME temp_model_site49
END GET_SERIES_SSF

# Read Time Series (Calibration data)
START GET_MUL_SERIES_SSF
   CONTEXT all
   FILE ../PEST/calibration_data.ssf
   SITE obs_1
   NEW_SERIES_NAME cal_site1
   SITE obs_2
   NEW_SERIES_NAME cal_site2
   SITE obs_3
   NEW_SERIES_NAME cal_site3
   SITE obs_4
   NEW_SERIES_NAME cal_site4
   SITE obs_5
   NEW_SERIES_NAME cal_site5
   SITE obs_6
   NEW_SERIES_NAME cal_site6
   SITE obs_7
   NEW_SERIES_NAME cal_site7
   SITE obs_8
   NEW_SERIES_NAME cal_site8
   SITE obs_9
   NEW_SERIES_NAME cal_site9
   SITE obs_10
   NEW_SERIES_NAME cal_site10
   SITE obs_11
   NEW_SERIES_NAME cal_site11
   SITE obs_12
   NEW_SERIES_NAME cal_site12
   SITE obs_13
   NEW_SERIES_NAME cal_site13
   SITE obs_14
   NEW_SERIES_NAME cal_site14
   SITE obs_15
   NEW_SERIES_NAME cal_site15
   SITE obs_16
   NEW_SERIES_NAME cal_site16
   SITE obs_17
   NEW_SERIES_NAME cal_site17
   SITE obs_18
   NEW_SERIES_NAME cal_site18
   SITE obs_19
   NEW_SERIES_NAME cal_site19
   SITE obs_20
   NEW_SERIES_NAME cal_site20
   SITE obs_21
   NEW_SERIES_NAME cal_site21
   SITE obs_22
   NEW_SERIES_NAME cal_site22
   SITE obs_23
   NEW_SERIES_NAME cal_site23
   SITE obs_24
   NEW_SERIES_NAME cal_site24
   SITE obs_25
   NEW_SERIES_NAME cal_site25
   SITE obs_26
   NEW_SERIES_NAME cal_site26
   SITE obs_27
   NEW_SERIES_NAME cal_site27
   SITE obs_28
   NEW_SERIES_NAME cal_site28
   SITE obs_29
   NEW_SERIES_NAME cal_site29
   SITE obs_30
   NEW_SERIES_NAME cal_site30
   SITE obs_31
   NEW_SERIES_NAME cal_site31
   SITE obs_32
   NEW_SERIES_NAME cal_site32
   SITE obs_33
   NEW_SERIES_NAME cal_site33
   SITE obs_34
   NEW_SERIES_NAME cal_site34
   SITE obs_35
   NEW_SERIES_NAME cal_site35
   SITE obs_36
   NEW_SERIES_NAME cal_site36
   SITE obs_37
   NEW_SERIES_NAME cal_site37
   SITE obs_38
   NEW_SERIES_NAME cal_site38
   SITE obs_39
   NEW_SERIES_NAME cal_site39
   SITE obs_40
   NEW_SERIES_NAME cal_site40
   SITE obs_41
   NEW_SERIES_NAME cal_site41
   SITE obs_42
   NEW_SERIES_NAME cal_site42
   SITE obs_43
   NEW_SERIES_NAME cal_site43
   SITE obs_44
   NEW_SERIES_NAME cal_site44
   SITE obs_45
   NEW_SERIES_NAME cal_site45
   SITE obs_46
   NEW_SERIES_NAME cal_site46
   SITE obs_47
   NEW_SERIES_NAME cal_site47
   SITE obs_48
   NEW_SERIES_NAME cal_site48
   SITE obs_49
   NEW_SERIES_NAME cal_site49
END GET_SERIES_SSF

# Interpolate Model Output to Calibration data
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site1
   TB_SERIES_NAME cal_site1
   NEW_SERIES_NAME model_site1
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site2
   TB_SERIES_NAME cal_site2
   NEW_SERIES_NAME model_site2
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site3
   TB_SERIES_NAME cal_site3
   NEW_SERIES_NAME model_site3
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site4
   TB_SERIES_NAME cal_site4
   NEW_SERIES_NAME model_site4
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site5
   TB_SERIES_NAME cal_site5
   NEW_SERIES_NAME model_site5
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site6
   TB_SERIES_NAME cal_site6
   NEW_SERIES_NAME model_site6
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site7
   TB_SERIES_NAME cal_site7
   NEW_SERIES_NAME model_site7
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site8
   TB_SERIES_NAME cal_site8
   NEW_SERIES_NAME model_site8
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site9
   TB_SERIES_NAME cal_site9
   NEW_SERIES_NAME model_site9
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site10
   TB_SERIES_NAME cal_site10
   NEW_SERIES_NAME model_site10
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site11
   TB_SERIES_NAME cal_site11
   NEW_SERIES_NAME model_site11
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site12
   TB_SERIES_NAME cal_site12
   NEW_SERIES_NAME model_site12
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site13
   TB_SERIES_NAME cal_site13
   NEW_SERIES_NAME model_site13
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site14
   TB_SERIES_NAME cal_site14
   NEW_SERIES_NAME model_site14
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site15
   TB_SERIES_NAME cal_site15
   NEW_SERIES_NAME model_site15
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site16
   TB_SERIES_NAME cal_site16
   NEW_SERIES_NAME model_site16
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site17
   TB_SERIES_NAME cal_site17
   NEW_SERIES_NAME model_site17
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site18
   TB_SERIES_NAME cal_site18
   NEW_SERIES_NAME model_site18
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site19
   TB_SERIES_NAME cal_site19
   NEW_SERIES_NAME model_site19
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site20
   TB_SERIES_NAME cal_site20
   NEW_SERIES_NAME model_site20
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site21
   TB_SERIES_NAME cal_site21
   NEW_SERIES_NAME model_site21
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site22
   TB_SERIES_NAME cal_site22
   NEW_SERIES_NAME model_site22
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site23
   TB_SERIES_NAME cal_site23
   NEW_SERIES_NAME model_site23
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site24
   TB_SERIES_NAME cal_site24
   NEW_SERIES_NAME model_site24
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site25
   TB_SERIES_NAME cal_site25
   NEW_SERIES_NAME model_site25
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site26
   TB_SERIES_NAME cal_site26
   NEW_SERIES_NAME model_site26
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site27
   TB_SERIES_NAME cal_site27
   NEW_SERIES_NAME model_site27
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site28
   TB_SERIES_NAME cal_site28
   NEW_SERIES_NAME model_site28
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site29
   TB_SERIES_NAME cal_site29
   NEW_SERIES_NAME model_site29
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site30
   TB_SERIES_NAME cal_site30
   NEW_SERIES_NAME model_site30
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site31
   TB_SERIES_NAME cal_site31
   NEW_SERIES_NAME model_site31
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site32
   TB_SERIES_NAME cal_site32
   NEW_SERIES_NAME model_site32
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site33
   TB_SERIES_NAME cal_site33
   NEW_SERIES_NAME model_site33
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site34
   TB_SERIES_NAME cal_site34
   NEW_SERIES_NAME model_site34
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site35
   TB_SERIES_NAME cal_site35
   NEW_SERIES_NAME model_site35
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site36
   TB_SERIES_NAME cal_site36
   NEW_SERIES_NAME model_site36
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site37
   TB_SERIES_NAME cal_site37
   NEW_SERIES_NAME model_site37
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site38
   TB_SERIES_NAME cal_site38
   NEW_SERIES_NAME model_site38
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site39
   TB_SERIES_NAME cal_site39
   NEW_SERIES_NAME model_site39
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site40
   TB_SERIES_NAME cal_site40
   NEW_SERIES_NAME model_site40
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site41
   TB_SERIES_NAME cal_site41
   NEW_SERIES_NAME model_site41
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site42
   TB_SERIES_NAME cal_site42
   NEW_SERIES_NAME model_site42
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site43
   TB_SERIES_NAME cal_site43
   NEW_SERIES_NAME model_site43
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site44
   TB_SERIES_NAME cal_site44
   NEW_SERIES_NAME model_site44
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site45
   TB_SERIES_NAME cal_site45
   NEW_SERIES_NAME model_site45
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site46
   TB_SERIES_NAME cal_site46
   NEW_SERIES_NAME model_site46
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site47
   TB_SERIES_NAME cal_site47
   NEW_SERIES_NAME model_site47
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site48
   TB_SERIES_NAME cal_site48
   NEW_SERIES_NAME model_site48
END NEW_TIME_BASE
START NEW_TIME_BASE 
   CONTEXT all
   SERIES_NAME temp_model_site49
   TB_SERIES_NAME cal_site49
   NEW_SERIES_NAME model_site49
END NEW_TIME_BASE

# write the time series
START LIST_OUTPUT 
   CONTEXT all 
   FILE tsproc_output.ssf
   SERIES_NAME model_site1
   SERIES_NAME model_site2
   SERIES_NAME model_site3
   SERIES_NAME model_site4
   SERIES_NAME model_site5
   SERIES_NAME model_site6
   SERIES_NAME model_site7
   SERIES_NAME model_site8
   SERIES_NAME model_site9
   SERIES_NAME model_site10
   SERIES_NAME model_site11
   SERIES_NAME model_site12
   SERIES_NAME model_site13
   SERIES_NAME model_site14
   SERIES_NAME model_site15
   SERIES_NAME model_site16
   SERIES_NAME model_site17
   SERIES_NAME model_site18
   SERIES_NAME model_site19
   SERIES_NAME model_site20
   SERIES_NAME model_site21
   SERIES_NAME model_site22
   SERIES_NAME model_site23
   SERIES_NAME model_site24
   SERIES_NAME model_site25
   SERIES_NAME model_site26
   SERIES_NAME model_site27
   SERIES_NAME model_site28
   SERIES_NAME model_site29
   SERIES_NAME model_site30
   SERIES_NAME model_site31
   SERIES_NAME model_site32
   SERIES_NAME model_site33
   SERIES_NAME model_site34
   SERIES_NAME model_site35
   SERIES_NAME model_site36
   SERIES_NAME model_site37
   SERIES_NAME model_site38
   SERIES_NAME model_site39
   SERIES_NAME model_site40
   SERIES_NAME model_site41
   SERIES_NAME model_site42
   SERIES_NAME model_site43
   SERIES_NAME model_site44
   SERIES_NAME model_site45
   SERIES_NAME model_site46
   SERIES_NAME model_site47
   SERIES_NAME model_site48
   SERIES_NAME model_site49
SERIES_FORMAT ssf
END LIST_OUTPUT

# write pest control file
START WRITE_PEST_FILES 
   CONTEXT pest_prep
   NEW_PEST_CONTROL_FILE ../PEST/pestfile.pst
   NEW_INSTRUCTION_FILE ../PEST/pest_instructionfile.ins
# link to general files 
   PARAMETER_GROUP_FILE ../PEST/pilot_points/parameter_groupfile.dat
   PARAMETER_DATA_FILE ../PEST/pilot_points/parameter_datafile.dat
   MODEL_COMMAND_LINE ../bin/model_command.bat
# Link to to template and model input files
   TEMPLATE_FILE ../PEST/pilot_points/permpp.dat.tpl
   MODEL_INPUT_FILE ../PEST/pilot_points/permpp.dat
# Time Series for Objective Function
   OBSERVATION_SERIES_NAME cal_site1
   MODEL_SERIES_NAME model_site1
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site2
   MODEL_SERIES_NAME model_site2
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site3
   MODEL_SERIES_NAME model_site3
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site4
   MODEL_SERIES_NAME model_site4
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site5
   MODEL_SERIES_NAME model_site5
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site6
   MODEL_SERIES_NAME model_site6
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site7
   MODEL_SERIES_NAME model_site7
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site8
   MODEL_SERIES_NAME model_site8
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site9
   MODEL_SERIES_NAME model_site9
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site10
   MODEL_SERIES_NAME model_site10
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site11
   MODEL_SERIES_NAME model_site11
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site12
   MODEL_SERIES_NAME model_site12
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site13
   MODEL_SERIES_NAME model_site13
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site14
   MODEL_SERIES_NAME model_site14
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site15
   MODEL_SERIES_NAME model_site15
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site16
   MODEL_SERIES_NAME model_site16
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site17
   MODEL_SERIES_NAME model_site17
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site18
   MODEL_SERIES_NAME model_site18
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site19
   MODEL_SERIES_NAME model_site19
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site20
   MODEL_SERIES_NAME model_site20
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site21
   MODEL_SERIES_NAME model_site21
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site22
   MODEL_SERIES_NAME model_site22
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site23
   MODEL_SERIES_NAME model_site23
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site24
   MODEL_SERIES_NAME model_site24
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site25
   MODEL_SERIES_NAME model_site25
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site26
   MODEL_SERIES_NAME model_site26
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site27
   MODEL_SERIES_NAME model_site27
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site28
   MODEL_SERIES_NAME model_site28
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site29
   MODEL_SERIES_NAME model_site29
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site30
   MODEL_SERIES_NAME model_site30
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site31
   MODEL_SERIES_NAME model_site31
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site32
   MODEL_SERIES_NAME model_site32
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site33
   MODEL_SERIES_NAME model_site33
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site34
   MODEL_SERIES_NAME model_site34
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site35
   MODEL_SERIES_NAME model_site35
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site36
   MODEL_SERIES_NAME model_site36
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site37
   MODEL_SERIES_NAME model_site37
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site38
   MODEL_SERIES_NAME model_site38
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site39
   MODEL_SERIES_NAME model_site39
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site40
   MODEL_SERIES_NAME model_site40
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site41
   MODEL_SERIES_NAME model_site41
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site42
   MODEL_SERIES_NAME model_site42
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site43
   MODEL_SERIES_NAME model_site43
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site44
   MODEL_SERIES_NAME model_site44
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site45
   MODEL_SERIES_NAME model_site45
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site46
   MODEL_SERIES_NAME model_site46
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site47
   MODEL_SERIES_NAME model_site47
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site48
   MODEL_SERIES_NAME model_site48
   SERIES_WEIGHTS_EQUATION 1
   OBSERVATION_SERIES_NAME cal_site49
   MODEL_SERIES_NAME model_site49
   SERIES_WEIGHTS_EQUATION 1
END WRITE_PEST_FILES
##############