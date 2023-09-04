import { ref } from 'vue'
import axios from 'axios'

export function useLoggedIn() {
    const isLoggedIn = ref(false);
  
    const checkStatus = async () => {
        isLoggedIn.value = false;
        await axios.get('http://localhost:1071/users/me', {withCredentials: true,})
        .then((response) => {
            if (response.status == 200){
                isLoggedIn.value = true;
            } else{
                isLoggedIn.value = false;
            }
        })
        .catch((error) => {
            isLoggedIn.value = false;
        })
    };
     // invoke the function
    checkStatus();
  
    return isLoggedIn;
  }
  