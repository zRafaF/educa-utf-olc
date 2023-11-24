"""
* This file was @generated using pocketbase-typegen and chat-GPT 3.5
"""
from enum import Enum

class Collections(Enum):
    Articles = "articles"
    ArticlesStats = "articles_stats"
    Attachments = "attachments"
    Chapters = "chapters"
    ChaptersStats = "chapters_stats"
    Tags = "tags"
    TotalUsersArticlesStats = "total_users_articles_stats"
    TotalUsersChaptersStats = "total_users_chapters_stats"
    Users = "users"
    UsersStats = "users_stats"

# Alias types for improved usability
IsoDateString = str
RecordIdString = str
HTMLString = str

# System fields
class BaseSystemFields:
    def __init__(self, id: RecordIdString, created: IsoDateString, updated: IsoDateString, collectionId: str, collectionName: Collections, expand=None):
        self.id = id
        self.created = created
        self.updated = updated
        self.collectionId = collectionId
        self.collectionName = collectionName
        self.expand = expand

class AuthSystemFields(BaseSystemFields):
    def __init__(self, email: str, emailVisibility: bool, username: str, verified: bool, id: RecordIdString, created: IsoDateString, updated: IsoDateString, collectionId: str, collectionName: Collections, expand=None):
        super().__init__(id, created, updated, collectionId, collectionName, expand)
        self.email = email
        self.emailVisibility = emailVisibility
        self.username = username
        self.verified = verified

# Record types for each collection
class ArticlesVisibilityOptions(Enum):
    public = "public"
    private = "private"

class ArticlesRecord:
    def __init__(self, title: str, document: str, user: RecordIdString, visibility: ArticlesVisibilityOptions, attachments=None, description=None, tags=None, views=None, views_day=None, views_month=None, views_week=None):
        self.attachments = attachments
        self.description = description
        self.document = document
        self.tags = tags
        self.title = title
        self.user = user
        self.views = views
        self.views_day = views_day
        self.views_month = views_month
        self.views_week = views_week
        self.visibility = visibility

class ArticlesStatsVisibilityOptions(Enum):
    public = "public"
    private = "private"

class ArticlesStatsRecord:
    def __init__(self, title: str, document: str, user: RecordIdString, visibility: ArticlesStatsVisibilityOptions, author_avatar=None, author_name=None, author_username=None, description=None, likes=None, tags=None, views=None):
        self.author_avatar = author_avatar
        self.author_name = author_name
        self.author_username = author_username
        self.description = description
        self.document = document
        self.likes = likes
        self.tags = tags
        self.title = title
        self.user = user
        self.views = views
        self.visibility = visibility

class AttachmentsRecord:
    def __init__(self, user: RecordIdString, article=None, files=None):
        self.article = article
        self.files = files
        self.user = user

class ChaptersVisibilityOptions(Enum):
    public = "public"
    private = "private"

class ChaptersRecord:
    def __init__(self, user: RecordIdString, visibility: ChaptersVisibilityOptions, articles=None, cover=None, description=None, tags=None, title=None, views=None, views_day=None, views_month=None, views_week=None):
        self.articles = articles
        self.cover = cover
        self.description = description
        self.tags = tags
        self.title = title
        self.user = user
        self.views = views
        self.views_day = views_day
        self.views_month = views_month
        self.views_week = views_week
        self.visibility = visibility

class ChaptersStatsVisibilityOptions(Enum):
    public = "public"
    private = "private"

class ChaptersStatsRecord:
    def __init__(self, user: RecordIdString, visibility: ChaptersStatsVisibilityOptions, articles=None, author_avatar=None, author_name=None, author_username=None, cover=None, description=None, likes=None, tags=None, title=None, views=None):
        self.articles = articles
        self.author_avatar = author_avatar
        self.author_name = author_name
        self.author_username = author_username
        self.cover = cover
        self.description = description
        self.likes = likes
        self.tags = tags
        self.title = title
        self.user = user
        self.views = views
        self.visibility = visibility

class TagsRecord:
    def __init__(self, name: str):
        self.name = name

class TotalUsersArticlesStatsRecord:
    def __init__(self, name: str, likes=None, num=None, username=None, views=None):
        self.likes = likes
        self.num = num
        self.username = username
        self.views = views

class TotalUsersChaptersStatsRecord:
    def __init__(self, name: str, likes=None, num=None, username=None, views=None):
        self.likes = likes
        self.num = num
        self.username = username
        self.views = views

class UsersCampusOptions(Enum):
    Apucarana = "Apucarana"
    Campo_Mourão = "Campo Mourão"
    Cornélio_Procópio = "Cornélio Procópio"
    Curitiba = "Curitiba"
    Dois_Vizinhos = "Dois Vizinhos"
    Francisco_Beltrão = "Francisco Beltrão"
    Guarapuava = "Guarapuava"
    Londrina = "Londrina"
    Medianeira = "Medianeira"
    Pato_Branco = "Pato Branco"
    Ponta_Grossa = "Ponta Grossa"
    Santa_Helena = "Santa Helena"
    Toledo = "Toledo"

class UsersRecord:
    def __init__(self, name: str, avatar=None, campus=None, course=None, description=None, favorite_articles=None, favorite_chapters=None, liked_articles=None, liked_chapters=None):
        self.avatar = avatar
        self.campus = campus
        self.course = course
        self.description = description
        self.favorite_articles = favorite_articles
        self.favorite_chapters = favorite_chapters
        self.liked_articles = liked_articles
        self.liked_chapters = liked_chapters
        self.name = name

class UsersStatsRecord:
    def __init__(self, name: str, avatar=None, description=None, n_of_articles=None, n_of_articles_likes=None, n_of_articles_views=None, n_of_chapters=None, n_of_chapters_likes=None, n_of_chapters_views=None, username=None):
        self.avatar = avatar
        self.description = description
        self.n_of_articles = n_of_articles
        self.n_of_articles_likes = n_of_articles_likes
        self.n_of_articles_views = n_of_articles_views
        self.n_of_chapters = n_of_chapters
        self.n_of_chapters_likes = n_of_chapters_likes
        self.n_of_chapters_views = n_of_chapters_views
        self.name = name
        self.username = username

# Response types include system fields and match responses from
class ArticlesResponse(BaseSystemFields):
    def __init__(self, title: str, document: str, user: RecordIdString, visibility: str, attachments=None, description=None, tags=None, views=None, views_day=None, views_month=None, views_week=None, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.title = title
        self.document = document
        self.user = user
        self.visibility = visibility
        self.attachments = attachments
        self.description = description
        self.tags = tags
        self.views = views
        self.views_day = views_day
        self.views_month = views_month
        self.views_week = views_week

class ArticlesStatsResponse(BaseSystemFields):
    def __init__(self, title: str, document: str, user: RecordIdString, visibility: ArticlesStatsVisibilityOptions, author_avatar=None, author_name=None, author_username=None, description=None, likes=None, tags=None, views=None, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.title = title
        self.document = document
        self.user = user
        self.visibility = visibility
        self.author_avatar = author_avatar
        self.author_name = author_name
        self.author_username = author_username
        self.description = description
        self.likes = likes
        self.tags = tags
        self.views = views

class AttachmentsResponse(BaseSystemFields):
    def __init__(self, user: RecordIdString, article=None, files=None, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.article = article
        self.files = files
        self.user = user

class ChaptersResponse(BaseSystemFields):
    def __init__(self, user: RecordIdString, visibility: ChaptersVisibilityOptions, articles=None, cover=None, description=None, tags=None, title=None, views=None, views_day=None, views_month=None, views_week=None, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.user = user
        self.visibility = visibility
        self.articles = articles
        self.cover = cover
        self.description = description
        self.tags = tags
        self.title = title
        self.views = views
        self.views_day = views_day
        self.views_month = views_month
        self.views_week = views_week

class ChaptersStatsResponse(BaseSystemFields):
    def __init__(self, user: RecordIdString, visibility: ChaptersStatsVisibilityOptions, articles=None, author_avatar=None, author_name=None, author_username=None, cover=None, description=None, likes=None, tags=None, title=None, views=None, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.user = user
        self.visibility = visibility
        self.articles = articles
        self.author_avatar = author_avatar
        self.author_name = author_name
        self.author_username = author_username
        self.cover = cover
        self.description = description
        self.likes = likes
        self.tags = tags
        self.title = title
        self.views = views

class TagsResponse(BaseSystemFields):
    def __init__(self, name: str, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.name = name

class TotalUsersArticlesStatsResponse(BaseSystemFields):
    def __init__(self, name: str, likes=None, num=None, username=None, views=None, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.name = name
        self.likes = likes
        self.num = num
        self.username = username
        self.views = views

class TotalUsersChaptersStatsResponse(BaseSystemFields):
    def __init__(self, name: str, likes=None, num=None, username=None, views=None, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.name = name
        self.likes = likes
        self.num = num
        self.username = username
        self.views = views

class UsersResponse(AuthSystemFields):
    def __init__(self, name: str, avatar=None, campus=None, course=None, description=None, favorite_articles=None, favorite_chapters=None, liked_articles=None, liked_chapters=None, expand=None):
        super().__init__(email=None, emailVisibility=None, username=None, verified=None, id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.name = name
        self.avatar = avatar
        self.campus = campus
        self.course = course
        self.description = description
        self.favorite_articles = favorite_articles
        self.favorite_chapters = favorite_chapters
        self.liked_articles = liked_articles
        self.liked_chapters = liked_chapters

class UsersStatsResponse(BaseSystemFields):
    def __init__(self, name: str, avatar=None, description=None, n_of_articles=None, n_of_articles_likes=None, n_of_articles_views=None, n_of_chapters=None, n_of_chapters_likes=None, n_of_chapters_views=None, username=None, expand=None):
        super().__init__(id=None, created=None, updated=None, collectionId=None, collectionName=None, expand=expand)
        self.name = name
        self.avatar = avatar
        self.description = description
        self.n_of_articles = n_of_articles
        self.n_of_articles_likes = n_of_articles_likes
        self.n_of_articles_views = n_of_articles_views
        self.n_of_chapters = n_of_chapters
        self.n_of_chapters_likes = n_of_chapters_likes
        self.n_of_chapters_views = n_of_chapters_views
        self.username = username

# Types containing all Records and Responses, useful for creating typing helper functions
class CollectionRecords:
    articles: ArticlesRecord
    articles_stats: ArticlesStatsRecord
    attachments: AttachmentsRecord
    chapters: ChaptersRecord
    chapters_stats: ChaptersStatsRecord
    tags: TagsRecord
    total_users_articles_stats: TotalUsersArticlesStatsRecord
    total_users_chapters_stats: TotalUsersChaptersStatsRecord
    users: UsersRecord
    users_stats: UsersStatsRecord

class CollectionResponses:
    articles: ArticlesResponse
    articles_stats: ArticlesStatsResponse
    attachments: AttachmentsResponse
    chapters: ChaptersResponse
    chapters_stats: ChaptersStatsResponse
    tags: TagsResponse
    total_users_articles_stats: TotalUsersArticlesStatsResponse
    total_users_chapters_stats: TotalUsersChaptersStatsResponse
    users: UsersResponse
    users_stats: UsersStatsResponse
