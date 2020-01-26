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
				sh 'mvn clean install'
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
				sh '''
					./sl analyze --app HSL --java --cpg --wait .
				'''
			}
		}

		stage ('ShiftLeft Agent Testing') {
			steps {
				sh 'sleep 5'
			}
		}
	}
}
