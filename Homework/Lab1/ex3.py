uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# conect to data base (mlab)
from pymongo import MongoClient
client = MongoClient(uri)
# Getting a Database
db = client.get_database()
# Getting a Collection
collection = db['posts']
# Creat a Documents
post = {
    'title': 'Lỡ...',
    'author': 'Nguyễn Khương Linh',
    'content': 
    '''...Mơ những chiều sưa nở trắng sân
Ôm trong lòng một câu thơ viết vội
Mạng ký túc vào Google không nổi
Mấy thằng lại chống Mỹ cùng Liên Xô
Mơ bạn bè cùng với thầy cô
Những tiết học toàn đi quậy phá
Mà giờ đây mỗi đứa mỗi ngả
Còn mình ta, lạc lõng bơ vơ
Mơ về người con gái năm xưa
Em tinh khôi trong tà áo trắng
Nét hồn nhiên mang cả trời nắng
Để hồn tôi chết lặng giữa đêm giông
Nhớ người xưa, cảnh cũ nao lòng
Nhớ cuộc tình chưa thành đã lỡ
Bỗng nhớ về câu thơ viết dở
Thôi thì đành... điền đại cho xong..'''
}
# Inserting a Document
collection.insert_one(post)