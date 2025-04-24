import { render, screen } from '@testing-library/react';
import App from './App';

test('renders app header', () => {
  render(<App />);
  const headerElement = screen.getByText(/음성 인식 애플리케이션/i);
  expect(headerElement).toBeInTheDocument();
});

test('renders recording buttons', () => {
  render(<App />);
  const startButton = screen.getByText(/녹음 시작/i);
  const stopButton = screen.getByText(/녹음 중지/i);
  expect(startButton).toBeInTheDocument();
  expect(stopButton).toBeInTheDocument();
});