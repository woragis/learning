-- objects
local user = {id='a1', name='samantha'}
print(user['id'], user['name'])
for k, v in ipairs(user) do
  print(k, v)
end

