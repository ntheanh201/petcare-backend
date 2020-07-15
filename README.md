# How the APIs works
## Get Menu Data : /menu
+ Dữ liệu: Mảng xâu
+ Ví dụ  :


## Get Logo: /logo
+ Dữ liệu : Mảng xâu
+ Ví dụ: 

Trong ví dụ thì là 1 object, tuy nhiên sẽ phải sửa lại nó là 1 mảng gồm các xâu chính là link đến hình ảnh

## Get SiteInfo: /datasite
+ Dữ liệu: 1 Object có các thuộc tính sau {copyright: String, description: String, name: String}
+ Example: 

## Get Slide: /sliders
+Dữ liệu: Mảng các Object
	++Mỗi object có các thuộc tính sau: {description: String, images (Mảng xâu - Giống như phần logo ), title: String, url: String}
+Ví dụ: 



## Get Products: /products
+ Data:  Mảng object	
	++ Mỗi object sẽ có các thuộc tính sau: {category: String (Loại mặt hàng ), shortDescription: String, descriptions: String, id: String, imageURLs (Mảng xâu ), name: String, price:Number, numberOfRate(số lượng đánh giá ):Number, averageRating: Double (đánh giá trung bình ), comments: (mảng các object - ở phần api riêng về getComment sẽ có chi tiết), isAvailable (hiện còn hàng không ), nameOfShop: String (tên shop bán đồ này ), wareHouseAddress: String (địa chỉ của kho hiện đang giữ sản phẩm ) }
+ Ví dụ : Chưa có. 

## Get Services: /services
+ Data: Giống như products

## Get Comments: /comments
+ Data: Mảng object
	++ Mỗi object gồm có các thuộc tính sau: {author: String, description: String, title: String, rate: Number , url: String (đường dẫn đến sản phẩm/dịch vụ được comment), articleName: String (tên của sản phẩm/dịch vụ được comment), createdAt: Date }
+ Ví dụ; Chưa có


## Get News: /news
+ Data: Mảng object
	++ Mỗi object gồm có các thuộc tính {descriptions: String, hashtag: Array of Strings, thumbnailImage: String, shortDescription: String, title: String, author: String, createdAt: Date, }

## Get Categories: /categories
Phân biệt ở dưới có 1 cái cũng là get Categories nhưng là của sản phẩm
GetCategories này là get list các loại có ở trang hiện có (như shop thú cưng, services, phòng khám,...)
+ Data: Mảng object: 
	++ Mỗi object có các thuộc tính (backgroundImage: String, description: String, image: String, title: String, url: String) 

Chú ý: Ở ví dụ còn thiếu thuộc tính URL. 

## Get Products Categories: /product-categories
Lấy các danh sách category của product (ví dụ như Đồ chơi, thức ăn, ...)
+ Data: Mảng object
	++ Mỗi object gồm có : {name: String, url: String}
11. getClinic: /clinics
+ Data: Mảng object
	++ Mỗi object gồm có : {name: String, special: String - cái này là chuyên khoa của phòng khám - nội hay ngoại, address: String}
Hiện tại mới nghĩ ra được có thể, có thể sau này sẽ update thêm sau

## Get Cart: /cart/:userID
Cái này là để lấy thông tin giỏ hàng. Dữ liệu trả về giống y hệt products

## Get Pets: /pets/:userID
Lấy thông tin của pet cho mỗi người dùng
+ Data: Mảng object
	++ Mỗi object gồm có {name: String, type: String, DateOfBirth: Date, Height: Number, Weight: Number}
Hiện tại mới nghĩ được thế, có thể sau này phải update thêm

## getOrders: /orders/:shopID
Lấy thông tin danh sách các order của shop
+ Data: Mảng object
	++ Mỗi object bao gồm có {orderID: String, name: String, type: String, purchasedOn: Date, customerName: String, customerPhone: String, ShipTo: String, BasePrice: Number, purchasedPrice: Number, status: String}

## Get Shop Products: /products/:shopID
Lấy danh sách sản phẩm theo shop
Dữ liệu trả về y như products

## GetShopInfo: /shop/:shopID
Lấy thông tin của shop: 
Dữ liệu trả về như trong classDiagram 

## GetUserInfo: /user/:userID
Dữ liệu trả về như trong classDiagram
18. getSalesAds: /sales/:shopID
Lấy thông tin về sự kiện giảm giá
Dữ liệu trả về như trong classDiagram

## How the authentication work
- how to get token: POST request to "/auth/jwt/create/" with a header contain "Content-Type: application/json",
POST request body include "username" and "password"
- returned token include 2 token: "access" token exist in 5 minutes, "refresh" token exist in 1 day
- when access token is expried, POST request to "auth/jwt/refresh/" with header contain "Content-Type: application/json", POST request body include "refresh" token, it gonna return "access" token back
- when request to url with authentication, put "Authorization: Bearer {}".format(access_token) to the request header
- get auth user:
    - access "auth/users/me/" for auth user information

## Update Authenticated User
- PATCH -> /auth/users/me/ : update non-sercured infomation, include avatar, url, id, username, display_name, phone_number, facebook, role, date_of_birth, description, email, user_gender, cover

- POST -> /auth/users/set_password/ : update pass word, body: new_password, re_new_password, current_password
