import colander


class ValidationPutClass(colander.MappingSchema):
    '''validate a clas data from json'''
    name = colander.SchemaNode(colander.String(15), missing=colander.drop)
    idclass = colander.SchemaNode(colander.Integer(), missing=colander.drop)



