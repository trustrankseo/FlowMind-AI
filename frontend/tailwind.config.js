/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        bg: "#0b0d10",
        panel: "#12151a",
        panel2: "#171b21",
        line: "#232830",
        dim: "#7c8794",
        accent: "#5eead4",
        accentDim: "#1c3a35",
        warn: "#f0b429",
        danger: "#f0546b",
      },
      fontFamily: {
        display: ["'Space Grotesk'", "sans-serif"],
        mono: ["'JetBrains Mono'", "monospace"],
      },
    },
  },
  plugins: [],
}
