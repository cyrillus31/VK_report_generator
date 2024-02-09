# VK_report_generator
This application allows you to generate PDF reports with personal information of all directly related users in VK social network and allows you to add related contacts from other social networks.

## Endpoints

Visit the Swagger docs at `/docs#`

### POST

`/addFriend?user_id=<int>`

This endpoint accepts the user object with the following expected structure:

```
{
  "id": 123456,
  "original_user_id": 654321,
  "social_network": "Social Network",
  "first_name": "Leopold",
  "last_name": "Bloom",
  "about": "Live in Dublin",
  "bdate": "16.06.1922"
}
```

### GET

`/getFriendsWithGroupsPDF?user_id=<int>`

This endpoint will send you back an **PDF** report containing information about all users related to the *user_id*. </br></br>


`/getFriendsWithGroupsREPORT?user_id=<int>`

This endpoint will send you back an **HTML** report containing information about all users related to the *user_id*.</br></br>


## Deploy

Set your ENV in [.env](/.env.example)  
From the root folder of the project run the following command:

```console
docker compose up -d
```

## Contact me

- Telegram [@cyrillus31](https://t.me/cyrillus31)  
- Email: [kirill.olegovich31@gmail.com](kirill.olegovich31@gmail.com)