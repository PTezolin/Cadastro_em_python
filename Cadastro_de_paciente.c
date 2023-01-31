#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <locale.h>
#define Tam 999

typedef struct cad {
    char nome[100], cpf[20], vacina[100], data[15]; 
    int numlote;
}Cadastro;

Cadastro cad[Tam];
int i = 0;
int vac = 0;

// _____________________________________________ Cadastro de Vacina _____________________________________________

void cadastro(){
    char op;
    do{
        printf("Informe o nome do paciente: ");
        fflush(stdin);
        gets(cad[vac].nome);
        printf("Informe o CPF, no formato \"xxx.xxx.xxx-xx\": ");
        fflush(stdin);
        gets(cad[vac].cpf);
        printf("Informe qual foi vacina aplicada: ");
        fflush(stdin);
        gets(cad[vac].vacina);
        printf("Informe a data, no formato \"xx/xx/xxxx\": ");
        fflush(stdin);
        gets(cad[vac].data);
        printf("Informe o lote da vacina: ");
        fflush(stdin);
        scanf("%d", &cad[vac].numlote);
        printf("*** Usuário cadastrado ***\n\n");
        vac++;
        printf("Você deseja continuar cadastrando pacientes [S/N]? ");
        fflush(stdin);
        scanf("%s", &op);
        printf("\n");
    } while (op == 'S' || op == 's');
    system("cls");  
}

// _____________________________________________ Lista de vacinado _____________________________________________

void lista(){
    char op;
    for (i = 0;i < vac;i++){
        printf("Código: %d\n", i+1);
        printf("Nome: %s\n",cad[i].nome);
        printf("CPF: %s\n",cad[i].cpf);
        printf("Vacina: %s\n",cad[i].vacina);
        printf("Data: %s\n",cad[i].data);
        printf("Número do lote: %d\n",cad[i].numlote);
        printf("====================================\n");
    }
    printf("\nPressione enter para voltar ao menu! ");
    getchar();
    if (getchar()){
        system("cls");
    }
}

// _____________________________________________ Pesquisa de cpf _____________________________________________

void pesquisa(){
    char pesquisacpf[20];
    char op;
    char busca = 0;
    do{
        printf("\nInforme o CPF que você deseja consultar, no formato \"xxx.xxx.xxx-xx\": ");
        fflush(stdin);
        gets(pesquisacpf);

        for (i = 0;i < vac;i++){
            if (strcmp(cad[i].cpf, pesquisacpf) == 0){
                busca = i;
                break;
            }
        }        
        if (i < vac){
            printf("\nOs dados referentes ao cpf %s digitado pelo usuário são: \n", pesquisacpf);
            printf("====================================\n");
            printf("Código: %d\n", i+1);
            printf("Nome: %s\n",cad[i].nome);
            printf("CPF: %s\n",cad[i].cpf);
            printf("Vacina: %s\n",cad[i].vacina);
            printf("Data: %s\n",cad[i].data);
            printf("Número do lote: %d\n",cad[i].numlote);
            printf("====================================\n");
        } else{
			system("cls");
            printf("\nO cpf que você buscou esta incorreto ou ainda não foi cadastrado!\n");
        }
        printf("\nVocê deseja consultar outro cpf [S/N]? ");
        fflush(stdin);
        scanf("%s", &op);
    } while (op == 'S' || op == 's');
    system("cls"); 
}

// ______________________________________________________________________________________________________________

int main(){
	setlocale(LC_ALL, "Portuguese");
    int escolha = 0;
    do{
    printf("-------------------------------------\n");
    printf("  Menu de aplicacão de vacinas:\n");
    printf("      1 - Cadastrar Vacina\n");
    printf("      2 - Listar Aplicacões\n");
    printf("      3 - Consultar por CPF\n");
    printf("      4 - Sair\n");
    printf("-------------------------------------\n");
    printf("Escolha uma opcão: ");
    scanf("%d",&escolha);
    switch (escolha){
        case 1: system("cls");   
                if (vac == Tam){
                    printf("\n*** Atencão: Banco de dados sem espaço! ***\n");
                    break;
                } 
                printf("------------------------------------------------------------\n");
                printf("                    Cadastro de Paciente                    \n");
                printf("------------------------------------------------------------\n");
                cadastro();
                break;
        case 2: system("cls");    
                printf("------------------------------------------------------------\n");
                printf("                     Lista de Pacientes                     \n");
                printf("------------------------------------------------------------\n");
                lista();
                break;
        case 3: system("cls");    
                printf("--------------------------------------------------------------------------------------\n");
                printf("                                     Consultar CPF                                    \n");
                printf("--------------------------------------------------------------------------------------");
                pesquisa();
                break;
        case 4: system("cls");    
                printf("------------------------------------------------------------\n");
                printf("                         Saindo ...                         \n");
                printf("------------------------------------------------------------\n");
                Sleep(3000);
                printf("O sistema foi encerrado ... \n");
                exit(0);
                break;
        default: system("cls"); 
                printf("O usuário escolheu uma opcão invalida, por favor informe corretamente!\n\n");
                break;
        }
    } while(escolha != 4);
    return 0;
}
