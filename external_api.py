import xmlrpc.client
#committttt
url = "http://localhost:8069"
db = "msuinterns"
username = "laxita"
password = "laxita"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print("Version infor",common.version())


uid = common.authenticate(db, username, password, {})

if uid:
    print("authentication success!")
else:
    print("authentication failed!")

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
products=models.execute_kw(db, uid, password, 'product.category', 'search', [[['name', '=', "01-SMD-S"]]]) #['email','=','1232@gmail.com'] {'offset':,'limit':}

products_count=models.execute_kw(db, uid, password, 'product.category', 'search_count', [[['name', '=', "01-SMD-S"]]])
print("product count",products_count)

print("---->",products)

# models.execute_kw(db, uid, password, 'product.category', 'search_count', [[['name', '=', "01-SMD-S"]]])
partner_rec = models.execute_kw(db, uid, password, 'product.category', 'read', [products],{'fields': ['name']})
print("--->",partner_rec)

partner_search_read=models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]], {'fields': ['name', 'import_export']})
print("---->",partner_search_read)

#create new record 
# vals={
#     'name':"New Partner"
# }

# created_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
# print("created a new record",created_id)

#update record
updated_name=models.execute_kw(db, uid, password, 'res.partner', 'write', [[11], {'name': "Newer partner"}])
print("name updated!")
# get record name after having changed it
# models.execute_kw(db, uid, password, 'res.partner', 'read', [[id], ['display_name']])

# records_fields=models.execute_kw(db, uid, password, 'product.category', 'fields_get', [], {'attributes': ['string', 'help', 'type']})
# print("---->",records_fields)