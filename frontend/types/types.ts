export interface BlogProps{
    "id": number,
    "title": string,
    "description": string,
    "display_image": string,
    "image_url": string,
    "slug": string,
    "published_at": string,
    "edited_at": string,
    "post_id": string,
    "comments": [
        {
            "id": number,
            "comment": string,
            "published_at": string,
            "edited_at": string,
            "post": number,
            "author": number,
            "sub_comments": []
        }
    ]
}