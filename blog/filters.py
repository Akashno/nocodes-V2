class ModelFilter():
    def __init__(self,model_objects,item):
        self.model_objects = model_objects
        self.item = item
        self.qs = []

    def filter(self):
        for post in self.model_objects:
            if self.item.lower() in str(post.title).lower():
                self.qs.append(post)
            if self.item.lower() in str(post.description).lower():
                self.qs.append(post)
            if self.item.lower() in str(post.author).lower():
                self.qs.append(post)

        return list(set(self.qs))