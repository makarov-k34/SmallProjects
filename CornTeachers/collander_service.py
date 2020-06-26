import colander


class Clas(colander.MappingSchema):
    '''for validation before insert'''
    fullname = colander.SchemaNode(colander.String(20),
                                   validator=colander.OneOf(['home', 'work']))
    number = colander.SchemaNode(colander.String())


