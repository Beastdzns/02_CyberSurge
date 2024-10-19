import { useEffect } from 'react';
import { NextPage } from 'next';

const CustomPage: NextPage = () => {
  useEffect(() => {
    // Redirect to the custom HTML file when the component mounts
    window.location.href = '/indian-tree.html';
  }, []);

  return null; // No content to render
};

export default CustomPage;