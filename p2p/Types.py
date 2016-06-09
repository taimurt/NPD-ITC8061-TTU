def enum(**enums):
	return type('Enum', (), enums)
	
Types = enum(
	VERIFYHANDLER = 1,
	MESSAGEHANDLER = 2
)

Types.ACKTYPE = b'00000100'