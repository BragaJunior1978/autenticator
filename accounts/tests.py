from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AutenticacaoTests(TestCase):

    def setUp(self):
        """Cria um usuário para os testes"""
        self.user = User.objects.create_user(username='Braga', password='Ab12345678*')

    def test_login_com_sucesso(self):
        """Teste de login bem-sucedido"""
        response = self.client.post(reverse('login'), {'username': 'Braga', 'password': 'Ab12345678*'})
        # Ajuste aqui: verifique a URL de redirecionamento correta
        expected_redirect_url = reverse('dashboard')  # Substitua 'dashboard' pela URL correta do painel
        self.assertRedirects(response, expected_redirect_url)

    def test_login_sem_sucesso(self):
        """Teste de login com senha errada"""
        response = self.client.post(reverse('login'), {'username': 'Braga', 'password': 'senhaerrada'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Credenciais inválidas')  # Ajuste para a mensagem correta

    def test_redirecionamento_para_cadastro(self):
        """Teste para verificar se o link 'Não tem conta? Cadastre-se' leva à página correta"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Criar Conta')
