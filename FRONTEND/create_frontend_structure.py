import os

base_dir = "src"

folders = [
    "assets",
    "components/cockpit",
    "components/transcript",
    "components/intelligence",
    "components/ui",
    "pages",
    "context",
    "services",
    "hooks",
    "routes",
    "layouts",
    "utils"
]

files = {
    "pages/Dashboard.jsx": "export default function Dashboard(){return <div>Dashboard</div>}",
    "pages/Interaction.jsx": "export default function Interaction(){return <div>Interaction</div>}",
    "pages/Escalation.jsx": "export default function Escalation(){return <div>Escalation</div>}",
    "pages/Login.jsx": "export default function Login(){return <div>Login</div>}",

    "context/AuthContext.jsx": """import {createContext} from 'react'
export const AuthContext = createContext()
""",

    "context/InteractionContext.jsx": """import {createContext} from 'react'
export const InteractionContext = createContext()
""",

    "context/SocketContext.jsx": """import {createContext} from 'react'
export const SocketContext = createContext()
""",

    "services/api.js": """import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5000/api'
})

export default api
""",

    "services/agraniService.js": "export const getCustomerBrief = ()=>{}",
    "services/vaniService.js": "export const processSpeech = ()=>{}",
    "services/smritiService.js": "export const getMemoryGraph = ()=>{}",
    "services/drishtiService.js": "export const scanDocument = ()=>{}",

    "hooks/useSocket.js": "export const useSocket = ()=>{}",

    "routes/AppRoutes.jsx": """import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Dashboard from '../pages/Dashboard'

export default function AppRoutes(){
return(
<BrowserRouter>
<Routes>
<Route path='/' element={<Dashboard/>}/>
</Routes>
</BrowserRouter>
)
}
""",

    "layouts/MainLayout.jsx": """export default function MainLayout({children}){
return(
<div className='min-h-screen bg-gray-100'>
{children}
</div>
)
}
""",

    "utils/helpers.js": "// helper functions here"
}


def create_structure():
    for folder in folders:
        path = os.path.join(base_dir, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    for file, content in files.items():
        path = os.path.join(base_dir, file)

        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(content)

            print(f"Created file: {path}")

if __name__ == "__main__":
    create_structure()
    print("\nSAARATHI Frontend structure created successfully 🚀")
    