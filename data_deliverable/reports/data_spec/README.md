# Data Specification

Our data is a collection of rowing data from the Brown Men's Crew Team. It is a collection of data which has been collected
both at the end of the 2022-2023 season and the beginning of the 2023-2024 season. The data is a subset of the whole data
which has been gathered on the team through the use of telemetry. The subset is based on a certain specific workout which
we complete often as a team. The data collected from the telemetry that is used in our dataset is described below.

#### Date

- The date of the workout
- Type: Date
- Format: MM/DD/YYYY
- Example: 01/01/2023
- Range: 03/22/2023 - 03/19/2024
- Distribution: The data is distributed evenly throughout the range
- Unique: No, there are multiple workouts on the same day
- Detection of duplicates: The date is not unique, but the combination of date and session number is unique so this can be used
to detect duplicates
- Required: Yes
- Use in analysis: No
- Sensitive information: No, the date is not sensitive

#### Box Number

- The number of the box used to record the data, unique to each box
- Type: Integer
- Format: 1234
- Example: 1234
- Range: 1111 - 9999
- Distribution: The data has four possible values for each of the four boxes
- Unique: Yes
- Detection of duplicates: The box number is unique to each box
- Required: Yes
- Use in analysis: No
- Sensitive information: No, the box number is not sensitive

#### Session Number

- The number of the session, unique to each session on each box
- Type: Integer
- Format: 123
- Example: 123
- Range: 100 - 999
- Distribution: The data has a range of 100 - 999, but the distribution is not uniform
- Unique: No, there is the probability of duplicates since each box can generate the same session number as another box
- Detection of duplicates: The combination of date and session number is unique so this can be used to detect duplicates
- Required: Yes
- Use in analysis: No
- Sensitive information: No, the session number is not sensitive

#### Piece Number

- The number of the piece, unique to each piece in each session for each box
- Type: Integer
- Format: 1
- Example: 1
- Range: 1 - 3
- Distribution: The data has a range of 1 - 3, each combination of date, session number, and piece number is unique
- Unique: Only for each combination of date, session number, and piece number
- Detection of duplicates: The combination of date, session number, and piece number is unique so this can be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the direction the boats were going at the time the data was recorded.
The data we have will mostly be used to compare boats at the same piece number. For piece number 1, 2 and 3 the boats will
always be going in the same direction so we can compare the boats at the same piece number. This allows
for some limitation of external factors such as wind and current.
- Sensitive information: No, the piece number is not sensitive

#### Seat

- The seat number of the rower, unique to each rower in each boat in each piece in each session for each box
- Type: Integer
- Format: 1
- Example: 1
- Range: 1 - 8
- Distribution: The data has a range of 1 - 8, each combination of date, session number, piece number, and seat is unique
- Unique: Only for each combination of date, session number, piece number, and seat
- Detection of duplicates: The combination of date, session number, piece number, and seat is unique so this can be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the rower who is in the seat at the time the data was recorded.
- Sensitive information: No, the seat number is not sensitive

#### Watts

- The power output of the rower, unique to each rower in each boat in each piece in each session for each box. The watts
is the power output of the rower at the time the data was recorded.
- Type: Integer
- Format: 123
- Example: 123
- Range: 0 - 999
- Distribution: The data has a range of 0 - 999, each combination of date, session number, piece number, seat, and watts is unique
- Unique: Only for each combination of date, session number, piece number, seat, and watts
- Detection of duplicates: The combination of date, session number, piece number, seat, and watts is unique so this can be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the power output of the rower at the time the data was recorded and will
be one of the metrics used to compare rowers.
- Sensitive information: No, the watts is not sensitive

#### Catch Angle

- The angle of the oar at the catch, unique to each rower in each boat in each piece in each session for each box. The catch angle
is the angle of the oar at the catch, ie: the angle of the oar at the beginning of the stroke.
- Type: Integer
- Format: -12
- Example: -55
- Range: -65 - -45
- Distribution: The data has a range of -65 - -45 but is not distributed evenly or normally in any way
- Unique: No, there is the probability of duplicates since each rower can generate the same catch angle as another rower
- Detection of duplicates: Cannot be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the angle of the oar at the catch at the time the data was recorded and will
be one of the metrics used to compare rowers.
- Sensitive information: No, the catch angle is not sensitive

#### Finish Angle

- The angle of the oar at the finish, unique to each rower in each boat in each piece in each session for each box. The finish angle
is the angle of the oar at the finish, ie: the angle of the oar at the end of the stroke.
- Type: Integer
- Format: 12
- Example: 30
- Range: 25 - 35
- Distribution: The data has a range of 25 - 35 but is not distributed evenly or normally in any way
- Unique: No, there is the probability of duplicates since each rower can generate the same finish angle as another rower
- Detection of duplicates: Cannot be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the angle of the oar at the finish at the time the data was recorded and will
be one of the metrics used to compare rowers.
- Sensitive information: No, the finish angle is not sensitive

#### Catch Slip

- The slip of the oar at the catch, unique to each rower in each boat in each piece in each session for each box. The catch slip
is the amount of slip of the oar at the catch, ie: the distance used to connect the oar to the water at the catch.
- Type: Integer
- Format: 12
- Example: 10
- Range: 0 - 20
- Distribution: The data has a range of 0 - 20 but is not distributed evenly or normally in any way
- Unique: No, there is the probability of duplicates since each rower can generate the same catch slip as another rower
- Detection of duplicates: Cannot be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the slip of the oar at the catch at the time the data was recorded and will
be one of the metrics used to compare rowers.
- Sensitive information: No, the catch slip is not sensitive

#### Finish Slip

- The slip of the oar at the finish, unique to each rower in each boat in each piece in each session for each box. The finish slip
is the amount of slip of the oar at the finish, ie: the distance between the oar losing connection and extracting it from the water.
- Type: Integer
- Format: 12
- Example: 10
- Range: 0 - 20
- Distribution: The data has a range of 0 - 20 but is not distributed evenly or normally in any way
- Unique: No, there is the probability of duplicates since each rower can generate the same finish slip as another rower
- Detection of duplicates: Cannot be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the slip of the oar at the finish at the time the data was recorded and will
be one of the metrics used to compare rowers.
- Sensitive information: No, the finish slip is not sensitive

#### Drive Length

- The length of the drive, unique to each rower in each boat in each piece in each session for each box. This is the difference between the catch and the finish angles.
- Type: Integer
- Format: 12
- Example: 90
- Range: 80 - 100
- Distribution: The data has a range of 80 - 100 but is not distributed evenly or normally in any way
- Unique: No, there is the probability of duplicates since each rower can generate the same drive length as another rower
- Detection of duplicates: Cannot be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the length of the drive at the time the data was recorded and will 
be one of the metrics used to compare rowers.
- Sensitive information: No, the drive length is not sensitive

#### Effective Length

- The effective length of the drive, unique to each rower in each boat in each piece in each session for each box. This is the length of the drive minus the catch slip and the finish slip.
- Type: Integer
- Format: 12
- Example: 90
- Range: 60 - 100
- Distribution: The data has a range of 60 - 100 but is not distributed evenly or normally in any way
- Unique: No, there is the probability of duplicates since each rower can generate the same effective length as another rower
- Detection of duplicates: Cannot be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the effective length of the drive at the time the data was recorded and will
be one of the metrics used to compare rowers.
- Sensitive information: No, the effective length is not sensitive

#### Rate

- The stroke rate, unique to each boat in each piece in each session for each box. This is the number of strokes per minute.
- Type: Integer
- Format: 12
- Example: 30
- Range: 20 - 40
- Distribution: The data has a range of 20 - 40 but is not distributed evenly or normally in any way
- Unique: No, there is the probability of duplicates since each boat can generate the same rate as another boat
- Detection of duplicates: Cannot be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the stroke rate of the boat at the time the data was recorded and will
be one of the metrics used to compare boats.
- Sensitive information: No, the rate is not sensitive

#### Speed

- The speed of the boat, unique to each boat in each piece in each session for each box. This is the speed of the boat averaged over the piece.
- Type: Float
- Format: 1.2
- Example: 5.3
- Range: 4.0 - 6.0
- Distribution: The data has a range of 4.0 - 6.0 but is not distributed evenly or normally in any way
- Unique: No, there is the probability of duplicates since each boat can generate the same speed as another boat
- Detection of duplicates: Cannot be used to detect duplicates
- Required: Yes
- Use in analysis: Yes, this will be used to determine the speed of the boat at the time the data was recorded and will
be one of the metrics used to compare boats.
- Sensitive information: No, the speed is not sensitive