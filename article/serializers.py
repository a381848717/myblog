from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    article_topic = serializers.ReadOnlyField(source="get_article_topic_display")
    status = serializers.ReadOnlyField(source="get_status_display")
    cn_status = serializers.SerializerMethodField()
    create_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        # 我们不希望用户自行修改id, author和create_date三个字段，我们把它们设成了仅可读read_only_fields。
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'article_title', 'create_date', 'author')
        depth = 1  # 注意这里

    def get_cn_status(self, obj):
        if obj.status == 'p':
            return "已发表"
        elif obj.status == 'd':
            return "草稿"
        else:
            return ''