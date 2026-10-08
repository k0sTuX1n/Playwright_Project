from playwright.sync_api import Page 

class Looks:
    def __init__(self, page : Page):
            self.page = page 
            self.knopka = page.get_by_role("link" , name = "Начать практику")
            self.текст_тут = page.get_by_placeholder("Введите текст здесь")
            self.Это_полеобязательнодлязаполнения = page.get_by_placeholder("Это поле обязательно для заполнения")
            self.Максимум = page.get_by_placeholder("Максимум 10 символов")

    def title(self):
          self.knopka.click()
          self.текст_тут.fill("Привет Мир ")
          self.Это_полеобязательнодлязаполнения.fill("Дмитрий")
          self.Максимум.fill("123456789")
        
          
          
          
          





