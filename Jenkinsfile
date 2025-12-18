pipeline {
    agent any

    options {
        skipDefaultCheckout()
    }

    parameters {
        string(
            name: 'NOMBRE',
            defaultValue: 'Celia Moreno Dionisio',
            description: 'Nombre del propietario'
        )

        choice(
            name: 'VAR_CHOICE',
            choices: ['Primera opción', 'Segunda opción'],
            description: 'Parámetro choice'
        )

        booleanParam(
            name: 'VAR_BOOL',
            defaultValue: true,
            description: 'Parámetro booleano'
        )

        file(
            name: 'ARCHIVO',
            description: 'Archivo de entrada para Python'
        )
    }

    environment {
        VENV = "venv"
    }

    stages {

        stage('Info inicial') {
            steps {
                echo "Hola, ${params.NOMBRE}"
                echo "El nombre del Pipeline de Jenkins es: ${env.JOB_NAME}"
                echo "El número de ejecución: ${env.BUILD_NUMBER}"
                echo "Carpeta donde Jenkins ejecuta tu pipeline: ${env.WORKSPACE}"
                echo "Opción elegida: ${params.VAR_CHOICE}"
            }
        }

        stage('Crear entorno virtual') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    python -m pip install --upgrade pip
                '''
            }
        }

        stage('Instalar requirements.txt') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Ejecutar Python') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    export NOMBRE="${NOMBRE}"
                    export VAR_CHOICE="${VAR_CHOICE}"

                    echo "Ruta real del archivo recibido: $ARCHIVO"

                    if [ -n "$ARCHIVO" ]; then
                        echo "Copiando archivo al workspace"
                        cp "$ARCHIVO" entrada.txt
                        echo "Archivos en workspace:"
                        ls -l
                        python3 python.py entrada.txt
                    else
                        echo "No se ha subido archivo. Ejecuto sin fichero."
                        python3 python.py
                    fi
                '''
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Credenciales') {
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

        stage('Condicional') {
            when {
                expression { params.VAR_BOOL }
            }
            steps {
                echo "VAR_BOOL es true, se ejecuta este stage"
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado."
        }
        success {
            echo "Se ha realizado el pipeline correctamente"
        }
        failure {
            echo "Algo ha fallado"
        }
    }
}
