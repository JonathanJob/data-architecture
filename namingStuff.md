# Naming stuff

Very essential in removing confusion for consumers of the data and for consistency across a system.

# Different schemas in the data processing pipeline

Bronze -> Silver -> Gold

RAW -> Processed -> Presentation

Stage -> DW -> Export

The initial stage can be appended with the system where it comes from to aid in some organization. As the second layer would typically involve joining these sources to create more merged datasets I would lean toward fewer named schemas or even one. The final stage can again have multiple different names as different consumers would require different views to the data.
