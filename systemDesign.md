# System Design

Considerations when designing a data system

## Graceful exits

Data systems need to handle errors effectively and allow for the restart of processess seamlessly. This is particularly problematic in multi step data procedures. If there are partial failures the reruns need to take this into account. Idemptency is very important here.

## Do I Need this data in this table

Pay attention to your table design. Do i need this column or these rows. Eg: We maintained 7 years of history in table that only needs a day's worth of data. This helps with join efficiency and manages size of indexes. This might not be applicable with well partitioned data. It still could be a concerns if the query needs to span across different nodes and does not work on the partition key.
