import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // Tudo que começa com /api vai para o Django (runserver em :8000).
    // Assim o front e o back parecem estar no mesmo endereço e não precisa de CORS.
    proxy: {
      '/api': 'http://127.0.0.1:8000',
    },
  },
})
