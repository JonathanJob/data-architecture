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

Event streaming is critical in asynchronous systems. Performing hand shakes as well as communicating data across different systems can be performed using event streaming systems like kafka or kinesis. These systems allow the subscribers to be technology agnostic of the publishers. This makes it easier to replace systems without having to care for interface apis changing. This makes it easier to test things locally as you do not have to standup variegated source systems. 
