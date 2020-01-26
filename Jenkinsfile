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
					python3 GetStatus.py --app "io.shiftleft-hello-shiftleft-jar" --version Vince
				'''
			}

			post {
				success {
					echo 'ShiftLeft Analysis Success!'
				}

				failure {
					echo 'ShiftLeft Analysis Failed!'
				}
			}
		}

		stage ('ShiftLeft Agent Testing') {
			steps {
				sh 'sleep 5'
			}

			post {
				success {
					echo 'Testing successful!'
				}

				failure {
					echo 'Testing failed!'
				}
			}
		}
	}
}
