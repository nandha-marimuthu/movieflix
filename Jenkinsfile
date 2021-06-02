node('minikube') {
    
     stage('test pipeline') {
        sh(script: """
            echo "hello"
           git clone https://github.com/nandha-marimuthu/movieflix.git
           cd ./movieflix
           
           docker build . -t test
        """)
    }
}
