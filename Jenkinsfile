pipeline {
    agent any

    parameters {
        string(
            name: 'VAR_STR',
            defaultValue: 'Valor por defecto',
            description: 'Parámetro string'
        )

        choice(
            name: 'VAR_CHOICE',
            choices: ['Primera opción', 'Segunda opción', 'Tercera opción'],
            description: 'Parámetro choice'
        )

        booleanParam(
            name: 'VAR_BOOL',
            defaultValue: true,
            description: 'Parámetro booleano'
        )
    }

    stages {

        stage('Primer pasito') {
            steps {
                echo "Valor de VAR_STR: ${params.VAR_STR}"
                echo "Opción elegida: ${params.VAR_CHOICE}"
            }
        }

        stage('Segundo pasito') {
            steps {
                sh '''
                    echo "hola gente" >> test.txt
                    echo "Archivo creado"
                '''
            }
        }

        stage('Tercer pasito (credenciales)') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'Celia_credencial',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )
                ]) {
                    sh '''
                        echo "Usuario: $USER"
                        echo "Password oculto correctamente"
                    '''
                }
            }
        }

        stage('Cuarto pasito (condicional)') {
            when {
                expression { params.VAR_BOOL }
            }
            steps {
                echo "VAR_BOOL es true, este stage se ejecuta"
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado"
        }
        success {
            echo "Pipeline exitoso ✅"
        }
        failure {
            echo "Pipeline fallido ❌"
        }
    }
} // <-- llave final que faltaba
