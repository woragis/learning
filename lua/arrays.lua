-- arrays
local colors = {'red', 'green', 'blue'}
print(colors[1]) -- first index
print(#colors) -- length of colors
table.insert(colors, 'orange') -- append
print(colors[4]) -- get 4th index

for i, v in ipairs(colors) do -- iteratable pair
  print("i: ",i," color: ",v,"!")
end

