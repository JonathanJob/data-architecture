# System Design

Considerations when designing a data system

## Graceful exits

Data systems need to handle errors effectively and allow for the restart of processess seamlessly. This is particularly problematic in multi step data procedures. If there are partial failures the reruns need to take this into account. Idemptency is very important here.
