describe('Audio Transcription App', () => {
    it('should load the homepage', () => {
      cy.visit('/');
      cy.contains('음성 인식 애플리케이션').should('be.visible');
    });
    
    it('should have recording buttons', () => {
      cy.visit('/');
      cy.contains('녹음 시작').should('be.visible');
      cy.contains('녹음 중지').should('be.visible');
    });
    
    it('should update UI when recording starts and stops', () => {
      cy.visit('/');
      cy.contains('녹음 시작').click();
      cy.contains('녹음이 시작되었습니다.').should('be.visible');
      cy.contains('녹음 중지').click();
      cy.contains('녹음이 중지되었습니다.').should('be.visible');
    });
  });