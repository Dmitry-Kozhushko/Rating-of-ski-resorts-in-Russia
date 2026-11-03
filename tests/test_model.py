import json
import pytest

def load_model_data():
    # Обрати внимание на '../data/' — это означает "выйти из папки tests и зайти в data"
    with open('../data/processed/model_data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def test_weights_sum():
    data = load_model_data()
    total_weight = sum(data['weights'].values())
    assert abs(total_weight - 100.0) < 0.001, "Сумма весов не равна 100!"

def test_scores_range():
    data = load_model_data()
    for row in data['model_rows']:
        for key, value in row.items():
            if key.endswith('_score') and isinstance(value, (int, float)):
                assert 0 <= value <= 100, f"Балл {key} вне диапазона 0-100 у {row['name_ru']}"

def test_row_count():
    data = load_model_data()
    assert len(data['model_rows']) == 32, "В таблице не 32 строки!"
    unique_ids = {row['resort_id'] for row in data['model_rows']}
    assert len(unique_ids) == 32, "Не 32 уникальных resort_id!"

def test_no_missing_trips():
    data = load_model_data()
    for row in data['model_rows']:
        assert row['trips_2025'] is not None, f"Пропуск trips_2025 у {row['name_ru']}"