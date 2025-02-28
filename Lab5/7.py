def to_camel(snake):
    parts = snake.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

print(to_camel("hello_world"))       
print(to_camel("snake_case_string"))  
print(to_camel("convert_this"))       

