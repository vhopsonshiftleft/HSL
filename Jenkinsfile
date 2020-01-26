pipeline {

	agent any

	stages {
		
		stage ('ShiftLeft Configuration') {
			steps {
				sh '''
				curl -O https://cdn.shiftleft.io/download/sl
				chmod +x sl
				'''
			}
		}

		stage ('Build') {
			steps {
				sh 'mvn clean build'
			}

			post {
				success {
					echo 'Maven Build success'
				}
				
				failure {
					echo 'Maven Build failure'
				}
			}
		}

		stage ('ShiftLeft Analysis') {
			steps {
				sh 'sleep 5'
			}
		}

		stage ('ShiftLeft Agent Testing') {
			steps {
				sh 'sleep 5'
			}
		}
	}
}
