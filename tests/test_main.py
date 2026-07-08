from src.main import main


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "Original Data:" in captured.out
    assert "Encrypted Data:" in captured.out
    assert "Compressed Data:" in captured.out
