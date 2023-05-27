class ContaBancaria:
    def __init__(self, Nome, NumDaConta, Saldo, TipoDaConta, Limite, StatusDaConta=False):
        self.Nome = Nome
        self.NumDaConta = NumDaConta
        self.Saldo = Saldo
        self.TipoDaConta = TipoDaConta
        self.Limite = Limite
        self.StatusDaConta = StatusDaConta



    def depositar(self, Quant):
        self.Saldo += Quant
        print(f"Foi depositado R${Quant:.2f}.")


    def sacar(self, Quant):
        self.Saldo -= Quant
        print(f"Você sacou R${Quant:.2f}.")

    def ativar_conta(self):
        if self.StatusDaConta == False:
            self.StatusDaConta = True
            print("Sua conta foi ativada.")


    def desativar_conta(self):
        if self.StatusDaConta == True:
            self.StatusDaConta = False
            print("Sua conta está desativada.")


    def verificar_saldo(self):
        print(f"O saldo total é R${self.Saldo:.2f}")

    def limite(self):
        if self.Saldo < 0:
            self.Limite -= self.Saldo
            print(f"Seu cheque especial é de R${self.Limite:.2f}.")


    def limite_usado(self, Quant): #Quant é o parâmetro do produto
        limite_total = 1000 - self.Limite #limite usado
        print(f"O total do seu limite é R${limite_total:.2f}.")
        limite_total += Quant # limite usado mais pagamento
        if limite_total >= 1000:
            deposito = limite_total - 1000 #limite total - 1000 é o que vai ser depositado na conta
            self.Saldo = deposito #deposito vai ser a nova quantidade de saldo
            limite_total -= self.Saldo #vai eliminar o o novo saldo do novo limite exemplo: eu paguei o que tava devendo, pro limite não ficar maior que mil (1050) eu vou tirar dele e vai ficar agora (1000).
            print(f"Seu novo saldo é R${self.Saldo:.2f} e o seu novo limite é R${limite_total:.2f}.")
        else:
            print("Pagamento menor que a quantidade negativada.")


Conta1 = ContaBancaria("Giovanna Giselli", 133620584, 500.56, "Corrente", 0, StatusDaConta=False)

Conta1.ativar_conta()
Conta1.depositar(400)
Conta1.sacar(950)
Conta1.verificar_saldo()
Conta1.limite()
Conta1.limite_usado(600)
