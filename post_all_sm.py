import argparse
import os

from dotenv import load_dotenv
import requests
import telegram
import vk_api


def main():
    load_dotenv()
    image_path, text_path = parse_img_and_txt_path()
    post_to_all_socmedia(image_path, text_path)


def parse_img_and_txt_path():
    parser = argparse.ArgumentParser(
        description='Программа опубликует пост во все соцсети'
    )
    parser.add_argument('img_path', help='Путь к изображению (рекомендуется jpeg)')
    parser.add_argument('txt_path', help='Путь к тексту')
    args = parser.parse_args()
    img_path = args.img_path
    txt_path = args.txt_path
    return img_path, txt_path


def post_to_all_socmedia(image_path, text_path):
    with open(text_path, 'r') as txt_file:
        text = txt_file.read()
    post_vkontakte(image_path, text)
    post_telegram(image_path, text)
    post_facebook(image_path, text)


def post_vkontakte(image_path, text):
    vk, upload = customize_vk_api()
    vk_group_id = os.getenv('VK_GROUP_ID')
    photo_id = vk_upload_photo(upload, image_path, vk_group_id)
    photo_name = f'photo-{vk_group_id}_{photo_id}'
    vk.wall.post(owner_id=f'-{vk_group_id}', message=text, attachments=photo_name)


def customize_vk_api():
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_api_version = '5.101'
    vk_session = vk_api.VkApi(token=vk_access_token, api_version=vk_api_version)
    vk = vk_session.get_api()
    upload = vk_api.VkUpload(vk_session)
    return vk, upload


def vk_upload_photo(upload, image_path, vk_group_id):
    vk_album_id = os.getenv('VK_ALBUM_ID')
    photo_info = upload.photo(
        image_path,
        album_id=vk_album_id,
        group_id=vk_group_id
        )
    photo_id = photo_info[0]['id']
    return photo_id


def post_telegram(image_path, text):
    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    chat_url = os.getenv('TG_CHAT_URL')
    bot = telegram.Bot(token=tg_bot_token)
    bot.send_message(chat_id=chat_url, text=text)
    with open(image_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_url, photo=photo)


def post_facebook(image_path, text):
    fb_group_id = os.getenv('FB_GROUP_ID')
    fb_token = os.getenv('FB_TOKEN')
    url = f'https://graph.facebook.com/{fb_group_id}/photos'
    payload = {
        'caption': text,
        'access_token': fb_token,
    }
    with open(image_path, 'rb') as photo:
        files = {'file': photo}
        response = requests.post(url, files=files, params=payload)
    response.raise_for_status()


if __name__ == '__main__':
    main()
