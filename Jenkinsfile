pipeline{
  agent any
  stages{
    stage('Pre-requisites') {
      steps {
	  bat 'py --version'
	  bat 'py -3 -mpip install Flask'
	  bat 'py -3 -mpip install flask_restful'
      }
    }
    environment{
	gitCredentialId = '1e079d86-3c8d-49be-a9e1-8aa21e661906'
	gitUrl = 'https://github.com/KrutikaVD/docker_project'
	deployBranch = 'main'
    }
    stage('Git checkout'){
      steps {
          git(
          url: gitUrl,
          credentialsId: gitCredentialId,
          branch: deployBranch
      )
    }
  }
    stage('Build Image'){
  	steps{
	  bat 'docker login -u="krutikavd" -p="Krutika&7"'
	  bat 'docker build -t base:0.2 .'
	  bat 'docker run -d -p 5000:5000 base:0.2'
      }
    }
  }
}