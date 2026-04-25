while running:
    screen.fill((0,0,0))
    fall_time += clock.get_rawtime()
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused   # toggle pause

    # 👇 STOP GAME WHEN PAUSED
    if not paused:
        if fall_time > 500:
            piece.move(0,1)
            if piece.collision():
                piece.move(0,-1)
                piece.merge()
                piece.clear_lines()
                piece = Piece()
            fall_time = 0

    draw_block()
    piece.draw()
    draw_grid()

    # 👇 SCORE DISPLAY
    score_text = font_small.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10,10))

    # 👇 PAUSE DISPLAY
    if paused:
        pause_text = font_small.render("PAUSED", True, (255,0,0))
        screen.blit(pause_text, (90,250))

    pygame.display.update()