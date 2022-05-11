# Data Architecture Concepts

## Abstraction

Abstractions in tooling are really important for productivity. It can get rid of a lot of boilerplate code and can make documentation a lot more concise and easier to parse through. Abstraction should not compromise flexibility. Abstractions through gui tools bring problems in like testing / cicd and version control.

Different developers like different level of abstractions. It is also use case dependent. For instance things like replication are much easier to do with a tool like AWS DMS. Handcoding that with python would be too laborious. I personally prefer to use python for most things unless the library does not support that function. A team should be cohesive in terms of the tooling that they use. Impossible to maintain if everyone does their own thing.

