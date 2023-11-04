# Instruction for Front End (API)
全部为 POST 类型接口，请求 body 为数据内容，内容格式为 JSON。
以下请求参数均需要以JSON格式包裹传输。

数据返回统一格式：
 - 请求成功样例：
    ```
    {
        "error" : null,
        "data": <请求结果>
    }
    ```
    下列接口规定中，仅说明 `data` 字段的内容.
 - 请求失败样例：
   ```
   {
        "error": <错误标识>,
        "message": <错误信息>
   }
   ```
   其中错误标识有：
      - BAD_REQUEST: 非法请求
      - NO_SUCH_PERSON_ID: 用户 id 不存在
      - NO_SUCH_PERSON_NAME： 用户名不存在
      - BAD_PHOTO: 图片上传失败
      - BAD_TOKEN：token 错误


## show_person_info/
 - url: `show_person_info/`
 - args:
    - name: 姓名，不分大小写，可以是名字的一部分。
 - resp:
    - 类型：array
    - 数组中每个元素为人的详细信息，注意这里仅返回已公开的人
 - example：
    - 请求内容:
        ```
        {
            "name" : "zhang"
        }
        ```
    - 响应内容：
        ```
        {
            "error": null,
            "data": [
                {
                    "id": 1,
                    "name": "Zhang Xin Yue 2",
                    "birthdate": "2023-10-10T00:00:00Z",
                    "photo_files": null,
                    "gender": null,
                    "lost_place": "Dong ying City",
                    "lost_date": null,
                    "family_name": "ShuYuMo",
                    "family_phone": "+60173526105",
                    "family_email": "244679245@qq.com",
                    "family_address": null,
                    "is_public": true
                },
                {
                    "id": 2,
                    "name": "Zhang Xin Yue 2",
                    "birthdate": "2023-10-10T00:00:00Z",
                    "photo_files": null,
                    "gender": null,
                    "lost_place": "Dong ying City",
                    "lost_date": null,
                    "family_name": "ShuYuMo",
                    "family_phone": "+60173526105",
                    "family_email": null,
                    "family_address": null,
                    "is_public": true
                }
            ]
        }
        ```

## save_or_update_person_info/
 - url: `save_or_update_person_info/`
 - args:
    - 需要传输一个人数据的所有字段，name字段必须有，其他不存在的字段会被设置为空（is_public 会被设置为 false），
    - 如果传输字段中有 `id` 则把请求理解为 **修改** ，否则理解为 **创建**。
 - resp:
    - 类型：Person
    - 这个人的当前信息。
 - example：
    - 创建（请求）：
     ```
     {
        "token": "ShuYuMo",
        "name": "Zhang Xin Yue 2",
        "birthdate": "2004-11-10",
        "photo_files": ["123.png"],
        "gender": "M",
        "lost_place": "Dong ying City",
        "lost_date": "2004-10-10",
        "family_name": "ShuYuMo",
        "family_phone": "+60173526105",
        "family_email": "123@qq.com",
        "family_address": "Shan Xi.",
        "is_public": true
    }
     ```
    - 创建（响应）：
     ```
     {
        "error": null,
        "data": {
            "id": 11,
            "name": "Zhang Xin Yue 2",
            "birthdate": "2004-11-10T00:00:00Z",
            "photo_files": [
                "123.png"
            ],
            "gender": "M",
            "lost_place": "Dong ying City",
            "lost_date": "2004-10-10",
            "family_name": "ShuYuMo",
            "family_phone": "+60173526105",
            "family_email": "123@qq.com",
            "family_address": "Shan Xi.",
            "is_public": false
        }
    }
     ```
    - 修改（请求）：
     ```
     {
        "token": "ShuYuMo",
        "id": 1,
        "name": "Zhang Xin Yue 2",
        "birthdate": "2004-11-10",
        "photo_files": ["123.png"],
        "gender": "M",
        "lost_place": "Dong ying City",
        "lost_date": "2004-10-10",
        "family_name": "ShuYuMo",
        "family_phone": "+60173526105",
        "family_email": "123@qq.com",
        "family_address": "Shan Xi.",
        "is_public": true
    }
     ```
    - 修改（响应）：
     ```
     {
        "error": null,
        "data": {
            "id": 1,
            "name": "Zhang Xin Yue 2",
            "birthdate": "2004-11-10T00:00:00Z",
            "photo_files": [
                "123.png"
            ],
            "gender": "M",
            "lost_place": "Dong ying City",
            "lost_date": "2004-10-10",
            "family_name": "ShuYuMo",
            "family_phone": "+60173526105",
            "family_email": "123@qq.com",
            "family_address": "Shan Xi.",
            "is_public": false
        }
     }
     ```

## set_public/
 - desc: 设置某一个用户的公开状态。
 - url: `set_public/`
 - args:
    - token: 验证字段，
    - id: 用户id
    - is_public: 设置为 什么公开状态 <boolen>
 - example:
    - 请求：
     ```
    {
        "token": "ShuYuMo",
        "id": 2,
        "is_public": false
    }
     ```
    - 响应：
     ```
    {
        "error": null,
        "data": "success"
    }
     ```

## get_all_person/
 - 获取所有用户信息（用于审核页）
 - url: `get_all_person/`
 - args:
    - token: 验证字段
 - resp:
    - array 类型，
    - 每个元素是人员信息，包括 is_public 字段。
 - example:
    - 请求：
      ```
      {
          "token" : "ShuYuMo"
      }
      ```
    - 响应：
      ```
      {
            "error": null,
            "data": [
                {
                    "id": 1,
                    "name": "Zhang Xin Yue 2",
                    "birthdate": "2004-11-10T00:00:00Z",
                    "photo_files": [
                        "123.png"
                    ],
                    "gender": "M",
                    "lost_place": "Dong ying City",
                    "lost_date": "2004-10-10",
                    "family_name": "ShuYuMo",
                    "family_phone": "+60173526105",
                    "family_email": "123@qq.com",
                    "family_address": "Shan Xi.",
                    "is_public": false
                },
                {
                    "id": 2,
                    "name": "Zhang Xin Yue 2",
                    "birthdate": "2004-11-10T00:00:00Z",
                    "photo_files": [
                        "123.png"
                    ],
                    "gender": "M",
                    "lost_place": "Dong ying City",
                    "lost_date": "2004-10-10",
                    "family_name": "ShuYuMo",
                    "family_phone": "+60173526105",
                    "family_email": "123@qq.com",
                    "family_address": "Shan Xi.",
                    "is_public": false
                },
                {
                    "id": 3,
                    "name": "Zhang Xin Yue",
                    "birthdate": "2023-10-09T00:00:00Z",
                    "photo_files": null,
                    "gender": null,
                    "lost_place": "Dong ying City",
                    "lost_date": null,
                    "family_name": "ShuYuMo",
                    "family_phone": "+60173526105",
                    "family_email": null,
                    "family_address": null,
                    "is_public": false
                },
                {
                    "id": 4,
                    "name": "Zhang Xin Yue",
                    "birthdate": "2023-10-09T00:00:00Z",
                    "photo_files": null,
                    "gender": null,
                    "lost_place": "Dong ying City",
                    "lost_date": null,
                    "family_name": "ShuYuMo",
                    "family_phone": "+60173526105",
                    "family_email": null,
                    "family_address": null,
                    "is_public": false
                },
                {
                    "id": 5,
                    "name": "Zhang Xin Yue",
                    "birthdate": "2023-10-09T00:00:00Z",
                    "photo_files": null,
                    "gender": null,
                    "lost_place": "Dong ying City",
                    "lost_date": null,
                    "family_name": "ShuYuMo",
                    "family_phone": "+60173526105",
                    "family_email": null,
                    "family_address": null,
                    "is_public": false
                }
            ]
        }
      ```

# upload_file/
 - desc: 上传图片
 - desc：不采用 JSON 格式，采用表单上传文件。文件对应字段名称为 'photo'，文件大小限制为 `10 MiB`, 文件类型限制为 ['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp', 'tiff']， 上传后返回服务器上文件名。
 - example:
 - 响应：
  ```
    {
        "error": null,
        "data": "4957ab42-7af2-11ee-8b40-01963c4ee1b4.png"
    }
  ```