from flask_bcrypt import generate_password_hash

password = 'mark@1234'

print(generate_password_hash(password))


