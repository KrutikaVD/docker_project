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
    stage('Git checkout'){
  	steps{
	  git 'https://github.com/KrutikaVD/docker_project'
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