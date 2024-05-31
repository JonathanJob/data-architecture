# Data Architecture Concepts

## Abstraction

Abstractions in tooling are really important for productivity. It can get rid of a lot of boilerplate code and can make documentation a lot more concise and easier to parse through. Abstraction should not compromise flexibility. Abstractions through gui tools bring problems in like testing / cicd and version control.

Different developers like different level of abstractions. It is also use case dependent. For instance things like replication are much easier to do with a tool like AWS DMS. Handcoding that with python would be too laborious. I personally prefer to use python for most things unless the library does not support that function. A team should be cohesive in terms of the tooling that they use. Impossible to maintain if everyone does their own thing.

Using the simplest abstraction required for that use case will allow us to get good performance with prodcutivity boosts. Higher leves of abstraction lead to more compromises.

## A/B testing

How can a/b testing be used in data architecture? Usability metrics can be collected for different published data sets to determine what type of datasets users are more likely to consume. What is important is to capture results and constantly iterate. Decisions made should be temporary and we should re-assess proven experiments.

## Idempotency

Running a task multiple times on the same input data will not affect the integrity of the output data. This is critical for a systems resiliency to failure. For timeseries data we should make sure duplicates are not entered. Files and events that are already processed must not be re-entered. This can be acheived through a primary key or by maintaining batch numbers to keep track of files or batch numbers that have already been processed. 

If it is type 1 data we need to make sure older data is not used to update more recent events. This can be done through maintaining timestamps.

## Event Streaming

Event streaming is critical in asynchronous systems. Performing hand shakes as well as communicating data across different systems can be performed using event streaming systems like kafka or kinesis. These systems allow the subscribers to be decoupled and technology agnostic of the publishers. This makes it easier to replace systems without having to care for interface apis changing. This makes it easier to test things locally as you do not have to standup variegated source systems.

This is also critical for microservice type applications where data needs to be integrated in real time for functionality like searches which would be more optimized when all data elements exist in a single store.

## KISS

Keep it simple st*p*d

A simple design is a lot better than a complicated one.

## ROI

Is the code providing an ROI.

### ROI for distributed vs single node processing systems

I have been exploring converting some of my pyspark transforms into polars code. Polars offers multithreaded processing that can outperform spark code for datasets of smaller sizes (<10M rows). This is especially true when using lazy frames. I am looking for ways of quantifying this in terms of an ROI.

## Lineage

Showing upstream data feeds that contribute data to the creation of the new dataset. Lineage can be very important to tracing the origins of data. It can also show how timing of upstream data feeds affect the timing of the target dataset. Also makes impact analysis easy when there are impacting changes to a data feed. Ability to view the transform logic that affects a particular dataset.

## Schema

What is the importance of schema to the processing efficiency of a data platform. For a really long time database systems adhered to a strict schema with data integrity checks. This allowed the platform to have a lot of information pertaining to the stored data. This allowed for stats collection and for query optimization.

Hadoop had a schema on read. Each row in the file on HDFS could have a different layout. This makes it more difficult to apply data integrity checks and to collect stats. 