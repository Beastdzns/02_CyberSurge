import { useEffect } from 'react';
import { NextPage } from 'next';

const UsMarkets: NextPage = () => {
  useEffect(() => {
    
    window.location.href = '/us-tree.html';
  }, []);

  return null; 
};  

export default UsMarkets;