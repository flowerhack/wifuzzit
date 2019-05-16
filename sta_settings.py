# Define variables
# SETTINGS is [ (STA_NUMBER, SAVE_RESULTS, SKIP) ]

TEST_SETTINGS_INDEX = 1

SETTINGS = [
            (0, 0, 0),
            (1, 0, 0),
            ]

# Defining the fuzzing MAC address device
AP_MAC  = "a4:c3:f0:94:7e:fb"

# Defining the injection interface
IFACE   = "wlp2s0"

##### BELOW VARIABLES SHOULD NOT BE TWEAKED BY THE USER

STA_NUMBER = SETTINGS[TEST_SETTINGS_INDEX][0]
SAVE_RESULTS = SETTINGS[TEST_SETTINGS_INDEX][1]
SKIP = SETTINGS[TEST_SETTINGS_INDEX][2]

# Defining fuzzing specific variables
STA = [ 
        #('44:07:0b:54:27:d2', 1),
        ('44:07:0b:62:bb:d1', 1),
        ('78:4f:43:a3:5a:5a', 1),
        ][STA_NUMBER]

STA_MAC = STA[0]
REPEAT_TIME = STA[1]

# Tuning listen value (fuzzing speed and false positive rates)
LISTEN_TIME = 60

# Defining the logging file
FNAME = [None, 'audits/sta-%s.session' % (STA_MAC)][SAVE_RESULTS]

# Defining the step value for IE fuzzing (should be odd to reach 255)
STEP    = [1, 3, 15, 17, 51][4]

# Defining the padding value
PADDING = "A"

# Defining truncate option
TRUNCATE = True

# Defining fuzzing specific variables
SSID    = "HelloFuzzerJulia"
CHANNEL = "\x01"                # Channel should be the same that real one
