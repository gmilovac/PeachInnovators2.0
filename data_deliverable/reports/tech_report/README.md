# Tech Report

## Questions

1. How many data points are there in total?

There are 992 unique data points in the dataset, each with 14 attributes that were manually transcribed into an Excel
spreadsheet over the course of ~20 hours.

2. What are the identifying attributes of the data?

The identifying attributes for each data point are the date, box number, piece number and session number.

3. Where is the data from?

    1. What are the attributes of the data?
       The attributes of the data are:
        - Date
        - Box
        - Piece
        - Session
        - Piece Number
        - Seat
        - Watts
        - Catch Angle
        - Finish Angle
        - Catch Slip
        - Finish Slip
        - Length
        - Effective Length
        - Stroke Rate
        - Speed
    2. Is the source of the data reliable?

   The source of the data is our coaches on the crew team. Since the data is directly gathered by them from a telemetry
   system, we believe the data is reliable.

    3. Describe the data sample?

   The data sample is a collection of 992 unique data points, each with 14 attributes. The data is collected from the
   Brown Men's Crew Team over the period of about a year. Each data point is a given athletes performance on a given
   day, in a given boat, in a given piece, in a given session. The data is collected from a telemetry system that
   records the athletes' performance in real time. The sample is a collection of the data points from the telemetry for
   a particular workout type, a 3x2000m open rate workout, which was used to keep the data consistent.
    4. Considerations for using the data?

   The data is anonymized, so there are no privacy concerns. The data is also collected from a telemetry system, so
   there are no concerns about the data being tampered with. The data is also collected from a consistent workout type,
   so there are no concerns about the data being inconsistent.

4. How clean is the data?
    1. How was the cleanliness of the data checked?

   The cleanliness of the data was checked by looking for missing values, duplicates, and data type issues. The data was
   manually transcribed from the telemetry system into an Excel spreadsheet, so it was checked for anomalies during that
   process. Any rows that would have included missing values were discarded. The data was also checked for duplicates
   and data type issues. The data was then cleaned by removing any rows that had missing values, duplicates, or data
   type issues.

    2. What was used to clean the data?

   The data was cleaned manually. Duplicate rows were removed by highlighting duplicate rows and removing them. Rows
   with missing values were removed by identifying them and removing them. Data type issues were resolved by
   identifying the issue and correcting it.

    3. Are there missing values in the data?

   There were some missing values in the data, which led to the removal of some rows. The missing values were in the
   `Watts`, `Catch Angle`, `Finish Angle`, `Catch Slip`, `Finish Slip`, `Length`, `Effective Length`, `Stroke Rate`,
   and `Speed` columns. The missing values were removed by removing the rows that had them.

    4. Are there any duplicates in the data?

   There were no duplicates in the data since the data is collected from a telemetry system.

    5. Are there any data type issues?

   There were no data type issues in the data since the data is collected from a telemetry system.

    6. Was any data discarded?

   Yes, some data was discarded. Rows with missing values were discarded, as well as duplicate rows. In some cases we
   decided not to use data that had clearly been recorded incorrectly. Examples of this include angles or power numbers
   that are not realistically feasible. This led to these sections of data not being recorded.

## Overall summary and observations

The data, at a glance seems to suggest that the obvious conclusion, that greater effective length and power output lead
to higher speeds, is true. The main challenge was actually entering the data into Excel which took a very long time as
it required a lot of manual entry. The data was then cleaned by removing any rows that had missing values, duplicates,
or data type issues. The next steps are to analyze the data to see if there are any interesting patterns or
correlations especially between effective length and power output and speed. We have not yet done this analysis, but we
plan to do so in the future.

