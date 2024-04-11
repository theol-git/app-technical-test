/** @type {import('next').NextConfig} */
const nextConfig = {
  distDir: "build",
  generateBuildId: async () => {
    return new Date().toDateString();
  },
};

export default nextConfig;
